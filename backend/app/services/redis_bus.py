import redis.asyncio as redis

from app.core.config import settings


class RedisBus:
    def __init__(self) -> None:
        self.client = redis.from_url(settings.redis_url, encoding='utf-8', decode_responses=True)

    async def publish(self, channel: str, payload: str) -> None:
        await self.client.publish(channel, payload)


redis_bus = RedisBus()
