import pandas as pd
from src.scraping import fetch_team_data

def build_dataframe(time: str, division: str): 
    dados = fetch_team_data(time, division)
    dados_filtrados = [d for d in dados if isinstance(d, dict) and 'ano' in d]

    if not dados_filtrados:
        raise ValueError(f"Nenhum dado válido encontrado para o time '{time}'.")

    estatisticas = sorted({k for d in dados_filtrados for k in d if k != 'ano'})
    df = pd.DataFrame(index=estatisticas)

    for d in sorted(dados_filtrados, key=lambda x: x['ano']):
        ano = str(d['ano'])
        df[ano] = pd.Series({k: d.get(k, 0) for k in estatisticas})

    df = df.apply(lambda col: col.map(lambda x: float(f"{x:.0f}")))
    df['Media'] = df.mean(axis=1).round(1)

    return df
