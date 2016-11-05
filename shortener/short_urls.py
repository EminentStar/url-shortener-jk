import uuid
import redis

from .base62_encoder import encode
from .base62_encoder import decode
from shortener.models import ShortUrl


redis_client = redis.StrictRedis(host='localhost', port=6379)


def create(origin_url):
    """
        short URL을 생성하는 메서드
        return:: short_url
    """
    uuid_key = uuid.uuid4()
    uuid_int = uuid_key.int
    short_url = encode(uuid_int)
   
    su = ShortUrl(uuid=str(uuid_key), short_url=short_url, original_url=origin_url)
    su.save()

    redis_client.set(uuid_key, origin_url)
    
    return short_url
