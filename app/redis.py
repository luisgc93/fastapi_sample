import redis
import sys


def redis_connect() -> redis.client.Redis:
    try:
        client = redis.Redis(
            host="192.168.1.138",
            port=6379,
            password="ubuntu",
            db=0,
            socket_timeout=5,
        )
        ping = client.ping()
        if ping is True:
            return client
    except redis.AuthenticationError:
        print("AuthenticationError")
        sys.exit(1)
