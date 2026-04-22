import os
from unittest import mock
from client.redis import MiddlewareSDKFacade
from client.redis.redis_conn import get_caching_data


@mock.patch('builtins.open')
def test_get_caching_data(mock_open):
    mock_file = mock.MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = """
    redis:
        host: localhost
        port: 6379
        password: mypassword
    """

    mock_open.return_value = mock_file
    os.environ['CONFIG_FILE'] = 'config.yaml'

    result = get_caching_data()

    assert result == {
        "CACHE_TYPE": "redis",
        "CACHE_REDIS_HOST": "localhost",
        "CACHE_REDIS_PORT": 6379,
        "CACHE_REDIS_URL": "redis://localhost:6379/0"
    }

    del os.environ['CONFIG_FILE']


@mock.patch('builtins.open')
def test_redis_status(mock_open):
    mock_file = mock.MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = """
    redis:
        host: localhost
        port: 6379
        password: mypassword
    """

    mock_open.return_value = mock_file
    os.environ['CONFIG_FILE'] = 'config.yaml'

    redis_client = MiddlewareSDKFacade.cache.redis_status()

    assert redis_client == "up"

    del os.environ['CONFIG_FILE']
