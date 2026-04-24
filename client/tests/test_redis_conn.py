from client.redis import MiddlewareSDKFacade
from client.redis.redis_conn import get_caching_data


def test_get_caching_data():
    result = get_caching_data()

    assert result["CACHE_TYPE"] == "redis"
    assert "CACHE_REDIS_HOST" in result
    assert "CACHE_REDIS_PORT" in result
    assert "CACHE_REDIS_URL" in result


def test_redis_status():
    facade = MiddlewareSDKFacade()
    result = facade.cache.redis_status()

    assert result == "up"
