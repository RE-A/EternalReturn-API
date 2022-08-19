from Client import Client

class ERUser:
    def __init__(self, api_client):
        self.username: str = ''
        self.usercode: str = ''
        self.client : Client = api_client


    def get_user(self, nickname:str):
        pass



