from aiohttp import web

routes = web.RouteTableDef()

@routes.get('/')
async def hello(request):
    print("serving home...")

    return web.FileResponse('./index.html')


app = web.Application()
app.add_routes(routes)

web.run_app(app)