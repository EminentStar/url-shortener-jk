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
        short_url = short_url.decode()
        return short_url
    else:
        try:
            short_url = ShortUrl.objects.get(original_url=origin_url).short_url
        except ShortUrl.DoesNotExist:
            guid = generate()
            short_url = encode(guid) 
            
            store_url_in_cache(short_url, origin_url)

            su = ShortUrl(guid=guid, short_url=short_url, original_url=origin_url)
            su.save()
        finally:
            return short_url


def shorturl(short_url):
    """
        shorturl의 기존 url을 찾아 리턴하는 함수
    """
    origin_url = redis_client.get("s" + short_url)

    if origin_url:
        origin_url = origin_url.decode()
        return origin_url
    else:
        try:
            guid = decode(short_url)
            origin_url = ShortUrl.objects.get(guid=guid).original_url
        except ShortUrl.DoesNotExist:
            origin_url ="Not Found"
        else:
            store_url_in_cache(short_url, origin_url)
        finally:
            return origin_url


def store_url_in_cache(short_url, origin_url):
    redis_client.set('s' + short_url, origin_url)
    redis_client.set('o' + origin_url, short_url)
            
