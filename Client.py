import json, requests
from requests import Response
from typing import Final


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

    def _request_get(self, req_target: str, params: dict) -> dict:
        url :str = self.BASE_API_URL + req_target
        resp: Response = requests.get(url, headers=self.headers, data=json.dumps(params))
        try:
            resp.raise_for_status()
        except Exception as e:
            print(e)  # TODO 에러 처리
        return resp.json()
