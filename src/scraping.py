from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from src.constants import TEAM_IDS, SEASONS, BASE_URL
import json


def fetch_team_data(time: str, division: str):
    division = division.upper()
    if division not in TEAM_IDS or time.lower() not in TEAM_IDS[division]:
        # Mensagem de erro mais informativa
        raise ValueError(f"Divisão ou time inválido: {time} ({division})")

    team_id = TEAM_IDS[division][time.lower()]
    serie = '325' if division == 'A' else '390'
    anos = list(range(2018, 2026))
    data_list = []

    # O driver e as opções são criados UMA VEZ, antes do loop.
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--log-level=3") # Reduz as mensagens "DevTools listening" no console.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    print(f"[SCRAPING] Iniciando busca de dados para {time.title()}...")

    # O bloco try...finally garante que o navegador seja fechado, mesmo se ocorrer um erro.
    try:
        # O loop agora apenas reutiliza o driver já existente.
        for season_id, ano in zip(SEASONS[division], anos):
            url = BASE_URL.format(team_id=team_id, serie=serie, season_id=season_id)

            driver.get(url)
            content = driver.find_element("tag name", "pre").get_attribute("innerText")
            
            # A lógica de processamento do JSON permanece a mesma
            response = json.loads(content)
            if 'statistics' in response:
                response['statistics']['ano'] = ano
                data_list.append(response['statistics'])
    finally:
        # O driver é fechado UMA VEZ, após o término de todas as buscas.
        driver.quit()
        print(f"[SCRAPING] Busca para {time.title()} finalizada.")

    return data_list
