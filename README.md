📊 Análise Estatística de Clubes do Brasileirão (Séries A e B)

Este projeto coleta, organiza e visualiza estatísticas históricas (2018–2025) de clubes das Séries A e B do Campeonato Brasileiro usando dados da API do SofaScore. As informações são apresentadas em tabelas e gráficos comparativos, permitindo análises de desempenho ao longo dos anos.

Como funciona

1. Escolha do Time
   O usuário informa o nome do clube e a divisão (A ou B). O sistema verifica a validade do time e carrega os dados da API do SofaScore para cada temporada.

2. Coleta de Dados
   Para cada temporada (de 2018 a 2025), o programa acessa a URL correspondente do SofaScore utilizando Selenium em modo "headless" e extrai os dados estatísticos via JSON.

3. Organização em DataFrame
   Os dados são convertidos em um DataFrame do pandas, contendo estatísticas por temporada e uma média final. Isso facilita a leitura e análise.

4. Visualização Gráfica
   O usuário pode comparar uma métrica específica (como gols, chutes, passes etc.) entre dois clubes ao longo dos anos por meio de gráficos de barras com Plotly.

Bibliotecas Utilizadas e Justificativas

selenium = Automatizar a navegação para acessar URLs protegidas e extrair o conteúdo da API.
Necessário para simular o acesso e capturar os dados do SofaScore, que exige carregamento em navegador.

webdriver_manager = Gerencia e atualiza automaticamente o driver do Chrome.
Evita erros de compatibilidade manual ao baixar drivers do Selenium.

json = Parseia o conteúdo JSON retornado pela API.
Os dados do SofaScore vêm em formato JSON, que precisa ser interpretado.

pandas = Organiza os dados em tabelas (DataFrames) e realiza cálculos.
Ideal para manipular estatísticas por ano, com cálculo de médias e estrutura tabular.

plotly.graph_objects = Cria gráficos interativos de barra para visualização comparativa.
Permite uma visualização clara e dinâmica dos dados entre clubes.

Exemplo de Uso

criar_grafico('goalsScored', 'flamengo', 'palmeiras')
Isso gerará um gráfico de barras comparando o número de gols entre Flamengo e Palmeiras de 2018 a 2025.
