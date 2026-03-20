from server import MicroEngine
from parser.response import Response
import time
import asyncio

app = MicroEngine()

@app.router.route("/", "GET")
def get_home_page(request):
    print(f"Request: {request.method} {request.path}")
    return Response(
        status_code=200, 
        status_message="OK", 
        headers={"Content-Type": "text/html"}, 
        message="<h1>Welcome to the Home Page</h1>"
    )

@app.router.route("/users", "GET")
async def get_all_users(request):
    print(f"Request: {request.method} {request.path}")
    await asyncio.sleep(10)
    return Response(
        status_code=200,
        status_message="Ok",
        headers={"Content-Type": "text/html"}, 
        message="<h1>All Users</h1><ol><li>Fabrice</li><li>Lassie</li><li>Simba</li><li>Cody</li></ol>"
    )

asyncio.run(app.start())