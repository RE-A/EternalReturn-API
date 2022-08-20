"""
간편한 한글 쿼리 작성
"""
from typing import Final


class APIQuery:
    # SHOTCUT : 제공된 API를 직관적으로 빠르게 추출하는 용도로 활용하는 키워드
    QUERY_SHOTCUT: Final[dict] = {'userid': {'query': r'user/nickname?query={query}',
                                             'params': 'query'},
                                  'toprank': {'query': r'rank/top/{seasonId}/{matchingTeamMode}',
                                              'params': ('seasonID', 'matchingTeamMode')},
                                  'userrank': {'query': r'rank/{usernum}/{seasonId}/{matchingTeamMode}',
                                               'params': ('usernum', 'seasonID', 'matchingTeamMode')},
                                  'userstats': {'query': r'user/stats/{usernum}/{seasonID}',
                                                'params': ('usernum', 'seasonID')},
                                  'matchhistory': {'query': r'user/games/{usernum}',
                                                   'params': ('usernum')},
                                  'matchresult': {'query': r'games/{gameID}',
                                                  'params': ('gameID')},
                                  'datatable': {'query': r'data/{metatype}',
                                                'params': ('metatype')},
                                  'language': {'query': r'i10n/{language}',
                                               'params': ('language')}
                                  }

    def __init__(self):
        pass
