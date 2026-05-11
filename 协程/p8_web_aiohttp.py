# Web Server
from aiohttp import web


#views
async def index(request):
    return web.Response(text='hettp aiohttp')


#routes
def setup_routes(app):
    app.router.add_get('/',index)

#app
app = web.Application()
setup_routes(app)
web.run_app(app,host='127.0.0.1',port=8080)
