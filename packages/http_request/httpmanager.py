import requests
from packages.utils.urlmanager import URLManager

class HttpManager:

    def __init__(self):
        self.__urlManager = URLManager()
        self.__redis_credentials = {}
        self.__access_code = ''
        pass
    
    def fetch_access_code(self):
        try:
            receive = requests.post(self.__urlManager.get_Url_Endpoint_Access_Code(), {})
            access_code = receive.text
            self.__set_access_code(access_code)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)       
    
    def fetch_init_data(self):
        credentials = {}
        try:
            receive = requests.post(self.__urlManager.get_Url_Endpoint(), {})
            response_data = receive.json()
            credentials = response_data['credentials']
            self.__set_redis_credentials(credentials)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    
    def __set_redis_credentials(self, credentials):
        self.__redis_credentials = credentials
    
    def get_redis_credentials(self):
        return self.__redis_credentials
    
    def __set_access_code(self, access_code):
        self.__access_code = access_code
    
    def get_access_code(self):
        return self.__access_code
        
        
        
            
        

