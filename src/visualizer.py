import plotly.graph_objects as go
from src.processor import build_dataframe


def plot_comparison(metric, time1, div1, time2, div2):
    try:
        df1 = build_dataframe(time1, div1)
        df2 = build_dataframe(time2, div2)
    except ValueError as e:
        print(f"[ERRO] {e}")
        return # Para a execução se não encontrar dados

    anos_validos = [
        str(ano) for ano in range(2018, 2026)
        if str(ano) in df1.columns and str(ano) in df2.columns
    ]

    if not anos_validos:
        print(f"[AVISO] Não há dados em comum para os anos analisados entre {time1.title()} e {time2.title()}.")
        return

    y1 = [df1.at[metric, ano] for ano in anos_validos]
    y2 = [df2.at[metric, ano] for ano in anos_validos]

    fig = go.Figure([
        go.Bar(name=time1.title(), x=anos_validos, y=y1),
        go.Bar(name=time2.title(), x=anos_validos, y=y2)
    ])
    fig.update_layout(
        title=f"Comparativo de '{metric.title()}' entre {time1.title()} e {time2.title()}",
        barmode='group'
    )
    fig.show(renderer="browser")
