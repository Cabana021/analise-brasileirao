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
    },
}

# IDs das temporadas
SEASONS = {
    'A': ['16183', '22931', '27591', '36166', '40557', '48982', '58766', '72034'],
    'B': ['16184', '22932', '27593', '36162', '40557', '49058', '59015', '72603'],
}

# URL base da API do SofaScore para obter estatísticas por time, divisão e temporada
BASE_URL = 'https://api.sofascore.com/api/v1/team/{team_id}/unique-tournament/{serie}/season/{season_id}/statistics/overall'
