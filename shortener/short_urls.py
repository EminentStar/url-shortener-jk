import basehash
import redis

from .base62 import encode 
from .base62 import decode
from .guid import generate
from shortener.models import ShortUrl


redis_client = redis.StrictRedis(host='localhost', port=6379)


def create(origin_url):
    """
        short URL을 생성하는 함수
        return:: short_url
    """

    short_url = redis_client.get("o" + origin_url)

    if short_url:
        return short_url
    else:
        try:
            short_url = ShortUrl.objects.get(original_url=origin_url).short_url
        except ShortUrl.DoesNotExist as err:
            print(err)
            
            

   
    guid = generate()
    short_url = encode(guid) 
    

    su = ShortUrl(guid=guid, short_url=short_url, original_url=origin_url)
    su.save()

    redis_client.set(uuid_key, origin_url)
    return short_url


def shorturl(short_url):
    """
        shorturl의 기존 url을 찾아 리턴하는 함수
    """
    uuid_int = decode(short_url)
    uuid_bytes = uuid_int.to_bytes(16, byteorder='big')
    uuid_key = uuid.UUID(bytes=uuid_bytes)
    uuid_str = str(uuid_key)
    
    origin_url = redis_client.get(uuid_str)

    if origin_url:
        origin_url = origin_url.decode()
        return origin_url
    else:
        try:
            origin_url = ShortUrl.objects.get(uuid=uuid_str).original_url
        except ShortUrl.DoesNotExist as err:
            print(err)
            return "Not Found"
        else:
            return origin_url
       
