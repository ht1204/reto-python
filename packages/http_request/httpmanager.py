import requests
from packages.utils.urlmanager import URLManager

class HttpManager:

    def __init__(self):
        self.__urlManager = URLManager()
        
        
    
    def fetch_init_data(self):
        load={}
        receive = requests.post(self.__urlManager.get_Url_Endpoint(), data=load)
        print(receive.json())
        print('________')
        credentials = receive.json()
        print(credentials['credentials'])
        

