from aiohttp import web
from service.views import get_messages, post_message


def setup_routes(app):
    app.add_routes([web.get('/', get_messages)])
    app.add_routes([web.post('/', post_message)])
