import requests
from packages.utils.urlmanager import URLManager

class HttpManager:

    def __init__(self):
        self.__urlManager = URLManager()
        
    
    def fetch_init_data(self):
        credentials = {}
        try:
            receive = requests.post(self.__urlManager.get_Url_Endpoint(), {})
            credentials = receive.json()
            return credentials
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        
            
        

