import json, requests
from requests import Response
from typing import Final

from query import APIQuery


class Client:
    BASE_URL: Final[str] = r"https://open-api.bser.io/"
    BASE_VERSION: Final[str] = r"v1/"
    BASE_API_URL: Final[str] = BASE_URL + BASE_VERSION


    def __init__(self, key: str, keytype: str ='private') -> None:
        """
        Save API key and set header
        :param key:
        """
        self.key: str = key
        if not keytype in ('private', 'production'):
            raise ValueError("API key type will be only 'private' or 'production'.")
        self.keytype : str= keytype
        self.headers: dict = {'x-api-key': self.key}

    def _request_get(self, req_url: str) -> dict:
        resp: Response = requests.get(req_url, headers=self.headers)
        try:
            resp.raise_for_status()
        except Exception as e:
            print(e)  # TODO 에러 처리
        return resp.json()

    def _request_post(self, req_url: str, params: dict) -> dict:
        resp: Response = requests.get(req_url, headers=self.headers, data=json.dumps(params))
        try:
            resp.raise_for_status()
        except Exception as e:
            print(e)  # TODO 에러 처리

        return resp.json()



    def query(self, query_name: str, params: dict[str:str]) -> dict:
        query_data: dict[str:str] = APIQuery.QUERY_SHOTCUT.get(query_name)
        dest_url : str = query_data.get('query').format(**params)
        for param_name in params:
            if param_name not in query_data['params']:
                raise ValueError("{param_name} should be exist.")

        query_url = self.BASE_API_URL + dest_url

        result = self._request_get(query_url)

        return result