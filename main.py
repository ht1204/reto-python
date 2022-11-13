import json
from packages.http_request.httpmanager import HttpManager
from packages.redis.redismanager import RedisManager
from packages.mongo.mongomanager import MongoManager
from packages.decrypt.decryptmanager import DecryptManager

class Main:
    
    def __init__(self):
        self.__retrieved_data = {}
        pass

    def start(self):
        http_manager = HttpManager()
        http_manager.fetch_init_data()
        redis_credentials = http_manager.get_redis_credentials()
        print('redis_credentials: ', json.dumps(redis_credentials, indent=4))

        redis_manager = RedisManager()
        redis_manager.redis_connection_pool(redis_credentials)
        
        mongo_credentials = redis_manager.get_mongo_credentials()
        print('mongo_credentials: ', json.dumps(mongo_credentials, indent=4))
   
           
        mongo_manager = MongoManager()
        mongo_manager.mongo_connection(mongo_credentials)
        code = mongo_manager.get_code()
        print('code: ', code)
        
        decrypter = DecryptManager()
        decrypter.decrypt(code)
        decoded = decrypter.get_decrypted()
        print('decoded: ', decoded)
        
        http_manager.fetch_access_code()
        access_code = http_manager.get_access_code()
        print('access_code: ', access_code)

            

###############################################

main = Main()
main.start()
