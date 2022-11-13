import pymongo
from pymongo import MongoClient

class MongoManager:
    
    def __init__(self):
        self.__code = ''
        pass
    
    def __create_mongo_cluster_url(self, mongo_credentials) -> str:
        mongo_cluster_params = [
            'mongodb+srv://', 
            mongo_credentials['username'],
            ':',
            mongo_credentials['password'],
            '@',
            mongo_credentials['host']          
            ]
        
        black_space=''
        mongo_url = black_space.join([str(item) for item in mongo_cluster_params])
        return mongo_url
        
    
    
    def mongo_connection(self, mongo_credentials):
        try: 
            mongo_url = self.__create_mongo_cluster_url(mongo_credentials)
            cluster = MongoClient(mongo_url)
            database = cluster['taller-mir']
            collection = database['instructions']
            mongo_data = collection.find_one()
            code = mongo_data['code']
            self.__set_code(code)
        except Exception as e:
            raise SystemExit(e)
    
    
    def __set_code(self, code):
        self.__code = code
    
    
    def get_code(self):
        return self.__code