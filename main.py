import json
from packages.http_request.httpmanager import HttpManager
from packages.redis.redismanager import RedisManager

def main():
    http_manager = HttpManager()
    redis_manager = RedisManager()
    
    redis_credentials = http_manager.fetch_init_data()
    print('redis_credentials: ', json.dumps(redis_credentials['credentials'], indent=4))
    
    redis_manager.redis_connection_pool(redis_credentials['credentials'])

main()