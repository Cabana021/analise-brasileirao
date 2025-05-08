📊 Análise Estatística de Clubes do Brasileirão (Séries A e B)

Este projeto coleta, organiza e visualiza estatísticas históricas (2018–2025) de clubes das Séries A e B do Campeonato Brasileiro usando dados da API do SofaScore. As informações são apresentadas em tabelas e gráficos comparativos, permitindo análises de desempenho ao longo dos anos.

Como funciona

1. Escolha do Time:
   O usuário informa o nome do clube e a divisão (A ou B). O sistema verifica a validade do time e carrega os dados da API do SofaScore para cada temporada.

2. Coleta de Dados:
   Para cada temporada (de 2018 a 2025), o programa acessa a URL correspondente do SofaScore utilizando Selenium em modo "headless" e extrai os dados estatísticos via JSON.

3. Organização em DataFrame:
   Os dados são convertidos em um DataFrame do pandas, contendo estatísticas por temporada e uma média final. Isso facilita a leitura e análise.

4. Visualização Gráfica:
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
Ao executar o programa (python main.py), o usuário será guiado por etapas interativas no terminal:

1. Digite o primeiro time:
Exemplo: flamengo

2. Digite o segundo time:
Exemplo: palmeiras

3. Informe a divisão do primeiro time:
Exemplo: A

4. Informe a divisão do segundo time:
Exemplo: A

5. Digite a métrica que deseja visualizar:
Exemplo: goalsScored

6. Indique se deseja continuar:
Exemplo: s (para fazer outra análise) ou n (para encerrar o programa)

Isso gerará automaticamente um gráfico de barras comparando o desempenho dos dois clubes na métrica escolhida (neste caso, "gols marcados") durante as temporadas de 2018 a 2025.

Exemplo de métrica
Você pode usar qualquer uma das métricas disponíveis na base de dados da API, como por exemplo:

goalsScored – Gols marcados

shotsOnTarget – Finalizações no alvo

ballPossession – Posse de bola

passes – Total de passes

yellowCards – Cartões amarelos

...entre outros (os nomes devem ser idênticos aos retornados pela API).