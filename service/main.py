import aiohttp
import ujson

from service.routes import setup_routes
from service.config import app_config


headers = {'Authorization': f'FlespiToken {app_config.flespi_token}'}


async def persistent_session(app):
    app['persistent_session'] = session = aiohttp.ClientSession(
        base_url=app_config.flespi_base_url,
        headers=headers,
        json_serialize=ujson.dumps,
    )
    yield
    await session.close()

app = aiohttp.web.Application()
setup_routes(app)

app.cleanup_ctx.append(persistent_session)

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=app_config.app_host, port=app_config.app_port)
