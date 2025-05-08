from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
import json
import pandas as pd
import plotly.graph_objects as go

# IDs dos clubes da série A e B 
TEAM_IDS = {
    'A': {
        'flamengo': '5981', 'palmeiras': '1963', 'bragantino': '1999',
        'cruzeiro': '1954', 'fluminense': '1961', 'internacional': '1966',
        'bahia': '1955', 'botafogo': '1958', 'ceara': '2001',
        'sao paulo': '1981', 'vasco': '1974', 'corinthians': '1957',
        'juventude': '1980', 'fortaleza': '2020', 'mirassol': '21982',
        'vitoria': '1962', 'atletico mg': '1977', 'gremio': '5926',
        'santos': '1968', 'sport': '1959',
    },
    'B': {
        'avai': '7315', 'cuiaba': '49202', 'vila nova': '2021',
        'coritiba': '1982', 'goias': '1960', 'crb': '22032',
        'athletico': '1967', 'america mg': '1973', 'remo': '2012',
        'novorizontino': '135514', 'chapecoense': '21845', 'ferroviaria': '35285',
        'atletico go': '7314', 'criciuma': '1984', 'operario': '39634',
        'athletic': '342775', 'botafogo sp': '1979', 'paysandu': '1997',
        'amazonas': '336664', 'volta redonda': '6982',
    }
}

# IDs das temporadas
SEASONS = {
    # 2018–2025
    'A': ['16183', '22931', '27591', '36166', '40557', '48982', '58766', '72034'],  
    'B': ['16184', '22932', '27593', '36162', '40557', '49058', '59015', '72603'],
}

# URL base da API do SofaScore para obter estatísticas por time, divisão e temporada
BASE_URL = 'https://api.sofascore.com/api/v1/team/{team_id}/unique-tournament/{serie}/season/{season_id}/statistics/overall'

# Coleta os dados estatísticos do time informado entre 2018 e 2025
def escolher_equipe(time: str):
    division = input('Em qual divisão o time está? (A ou B) ').strip().upper()
    if division not in TEAM_IDS or time.lower() not in TEAM_IDS[division]:
        raise ValueError("Divisão ou time inválido.")

    team_id = TEAM_IDS[division][time.lower()]
    serie = '325' if division == 'A' else '390'
    anos = list(range(2018, 2026))
    data_list = []

    for season_id, ano in zip(SEASONS[division], anos):
        url = BASE_URL.format(team_id=team_id, serie=serie, season_id=season_id)

        # Configura o Chrome em modo headless para buscar os dados JSON
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(url)
        content = driver.find_element("tag name", "pre").get_attribute("innerText")
        driver.quit()

        response = json.loads(content)
        if 'statistics' in response:
            response['statistics']['ano'] = ano
            data_list.append(response['statistics'])

    return data_list

# Constrói um DataFrame com as estatísticas por ano do time selecionado
def criar_dataframe(time: str): 
    dados = escolher_equipe(time)
    dados_filtrados = [d for d in dados if isinstance(d, dict) and 'ano' in d]

    if not dados_filtrados:
        raise ValueError(f"Nenhum dado válido encontrado para o time '{time}'.")

    estatisticas = sorted({k for d in dados_filtrados for k in d if k != 'ano'})
    df = pd.DataFrame(index=estatisticas)

    # Adiciona os dados ano a ano ao DataFrame
    for d in sorted(dados_filtrados, key=lambda x: x['ano']):
        ano = str(d['ano'])
        df[ano] = pd.Series({k: d.get(k, 0) for k in estatisticas})

    # Formata os valores e adiciona a média final
    df = df.apply(lambda col: col.map(lambda x: float(f"{x:.0f}")))
    df['Media'] = df.mean(axis=1).round(1)

    return df

# Gera um gráfico de barras comparando uma métrica específica entre dois times
def criar_grafico(metric, time1, time2):
    df1 = criar_dataframe(time1)
    df2 = criar_dataframe(time2)

    anos = [str(ano) for ano in range(2018, 2026)]
    anos_validos = [ano for ano in anos if ano in df1.columns and ano in df2.columns]

    y1 = [df1.at[metric, ano] for ano in anos_validos]
    y2 = [df2.at[metric, ano] for ano in anos_validos]

    fig = go.Figure([
        go.Bar(name=time1.title(), x=anos_validos, y=y1),
        go.Bar(name=time2.title(), x=anos_validos, y=y2)
    ])
    fig.update_layout(title=metric.title(), barmode='group')
    fig.show()

# Execução principal do programa
if __name__ == "__main__":
    while True:
        # Coleta os times e a métrica desejada do usuário
        time1 = input("Digite o primeiro time: ").strip().lower() # Pede a primeira equipe
        time2 = input("Digite o segundo time: ").strip().lower() # Pede a segunda equipe
        metrica = input("Digite a métrica que deseja visualizar (ex: goals, shotsOnTarget): ").strip() # Pede a estatística que será comparada

        # Chama a função para criar o gráfico com os dados informados anteriormente
        criar_grafico(metrica, time1, time2)

        # Pergunta se o usuário deseja continuar ou encerrar
        continuar = input("\nDeseja fazer outra análise? (s/n): ").strip().lower()
        if continuar != 's':
            print("Encerrando o programa. Obrigado por usar!")
            break
