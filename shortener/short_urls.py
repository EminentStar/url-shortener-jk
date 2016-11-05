import basehash
import uuid
import redis

from .base62_encoder import encode
from .base62_encoder import decode
from shortener.models import ShortUrl


base62 = basehash.base62()

redis_client = redis.StrictRedis(host='localhost', port=6379)


def create(origin_url):
    """
        short URL을 생성하는 함수
        return:: short_url
    """
    uuid_key = uuid.uuid4()
    uuid_int = uuid_key.int
    short_url = base62.encode(uuid_int)
       
    su = ShortUrl(uuid=str(uuid_key), short_url=short_url, original_url=origin_url)
    su.save()

    redis_client.set(uuid_key, origin_url)
    print("uuid_str: %s" % str(uuid_key))    
    return short_url


def shorturl(short_url):
    """
        shorturl의 기존 url을 찾아 리턴하는 함수
    """
    uuid_int = base62.decode(short_url)
    uuid_bytes = uuid_int.to_bytes(16, byteorder='big')
    uuid_key = uuid.UUID(bytes=uuid_bytes)
    uuid_str = str(uuid_key)
    
    origin_url = redis_client.get(uuid_str)
    
    print("uuid_str: %s" % uuid_str)

    if origin_url:
        origin_url = origin_url.decode()
        print(origin_url)
        return origin_url
    else:
        try:
            origin_url = ShortUrl.objects.get(uuid=uuid_str).original_url
        except ShortUrl.DoesNotExist as err:
            print(err)
            return "Not Found"
        else:
            return origin_url
       
