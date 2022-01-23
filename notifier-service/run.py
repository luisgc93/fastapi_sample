import logging.config

from app.redis import redis_connect


logging.config.fileConfig("config/logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

redis = redis_connect()
pub_sub = redis.pubsub()
pub_sub.subscribe("book-published")

running = True


def send_notification():
    while running:
        message = pub_sub.get_message()
        if message:
            logger.info(f"Found message: {message['data']}")


def main():
    send_notification()


if __name__ == "__main__":
    main()
