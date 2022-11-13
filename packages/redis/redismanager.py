import redis
import json

class RedisManager:
    def __init__(self):
        pass
    
    def redis_connection_pool(self, redis_credentials):
        redis_pool = redis.StrictRedis(
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
        
        print('mongo_credentials: ', json.dumps(mongo_credentials, indent=4))