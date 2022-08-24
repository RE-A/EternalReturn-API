"""
간편한 한글 쿼리 작성
"""
from typing import Final
from GameData import Dataset


class APIQuery:

    def __init__(self):
        self.monster_set = Dataset.monster_set
        self.equip_set = Dataset.equip_set
        self.mastery_set = Dataset.mastery_set
        self.matching_mode = Dataset.matching_mode


    # SHOTCUT : 제공된 API를 직관적으로 빠르게 추출하는 용도로 활용하는 키워드
    # 추후 쿼리 조립시, F-string을 이용하여 {} 부분을 채워넣기 위해 _params로 지정.
    QUERY_SHOTCUT: Final[dict] = {'usernum': {'query': 'user/nickname?query={nickname}',
                                             'params': 'nickname'},
                                  'toprank': {'query': 'rank/top/{seasonId}/{matchingTeamMode}',
                                              'params': ('seasonID', 'matchingTeamMode')},
                                  'userrank': {'query': r'rank/{usernum}/{seasonId"}/{matchingTeamMode}',
                                               'params': ('usernum', 'seasonID', 'matchingTeamMode')},
                                  'userstats': {'query': r'user/stats/{usernum}/{seasonId}',
                                                'params': ('usernum', 'seasonID')},
                                  'matchlog': {'query': r'user/games/{usernum}',
                                                   'params': ('usernum')},
                                  'matchresult': {'query': r'games/{gameID}',
                                                  'params': ('gameID')},
                                  'datatable': {'query': r'data/{_params["metatype"]}',
                                                'params': ('metatype')},
                                  'language': {'query': r'i10n/{_params["language"]}',
                                               'params': ('language')}
                                  }

    def _beautify_game(self, game : dict):
        pass

    def beautify_matchlog(self, resp : dict) -> dict:
        """
        matchlog API로부터 나온 데이터를 정리

        :param resp: 응답을 dict화한 원본
        :return:
        """

        games = resp.get('userGames')
        beautify_games = [self._beautify_game for game in games]






