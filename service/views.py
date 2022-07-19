from aiohttp import web
import ujson
from json.decoder import JSONDecodeError

from service.config import app_config


async def get_messages(request):
    session = request.app['persistent_session']
    async with session.get(app_config.flespi_messages_url) as response:
        payload = await response.json()
        return web.Response(text=ujson.dumps(payload))


async def post_message(request):
    session = request.app['persistent_session']
    try:
        payload = await request.json()
    except JSONDecodeError:
        return web.Response(status=400, reason='Check the body of the request')
    async with session.post(app_config.flespi_messages_url, data=ujson.dumps(payload)) as responce:
        await responce.json()
        return web.Response(status=responce.status)
