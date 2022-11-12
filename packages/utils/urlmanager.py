
class URLManager:
    
    def __init__(self):
        self.__URL_ENDPOINT_INSTRUCTIONS = 'https://taller-node-http-dbs.herokuapp.com/taller-mir'
        self.__URL_ENDPOINT_ACCESS_CODE = 'https://taller-node-http-dbs.herokuapp.com/access-code'



    def get_Url_Endpoint(self) -> str:
        return self.__URL_ENDPOINT_INSTRUCTIONS

    def get_Url_Endpoint_Access_Code(self) -> str:
        return self.__URL_ENDPOINT_ACCESS_CODE
    
