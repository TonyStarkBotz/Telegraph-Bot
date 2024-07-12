from aiohttp import web

Tony_TelegraphBot = web.RouteTableDef()

@Tony_TelegraphBot.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Tony_TelegraphBot")


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(Tony_TelegraphBot)
    return web_app
  
