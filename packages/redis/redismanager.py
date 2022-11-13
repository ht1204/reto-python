import redis

class RedisManager:
    
    def __init__(self):
        self.__mongo_credentials = {}
        pass
    
    def redis_connection_pool(self, redis_credentials):
        try:
            redis_pool = redis.Redis(
                host=redis_credentials['host'],
                port=redis_credentials['port'],
                username=redis_credentials['user'],
                password=redis_credentials['password'],
                decode_responses=True)
            
            mongo_cluster_host = redis_pool.get('host')
            mongo_username = redis_pool.get('username')
            mongo_password = redis_pool.get('password')
            
            mongo_credentials = {
                'host': mongo_cluster_host,
                'username': mongo_username,
                'password': mongo_password
            }
            self.__set_mongo_credentials(mongo_credentials)
        except redis.exceptions.ConnectionError as e:
            raise SystemExit(e)
            
        
    def __set_mongo_credentials(self, mongo_credentials):
        self.__mongo_credentials = mongo_credentials
    
    def get_mongo_credentials(self):
        return self.__mongo_credentials
        
    
