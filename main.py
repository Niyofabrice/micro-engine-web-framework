import asyncio

from models import Fruit, User
from parser.response import Response
from server import MicroEngine

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

@app.router.route("/user", "POST")
def create_user(request):
    print(f"Request: {request.method} {request.path}")
    user = User()
    if request.body:
        if request.body.get("name"):
            user.name = request.body.get("name")
            user.save()
            return Response(
                status_code=201,
                status_message="Created",
                headers={"Content-Type": "text/html"},
                message=f"{user} added successfully"
            )
    return Response(
        status_code=400,
        status_message="Bad Request",
        headers={"Content-Type": "text/html"},
        message="Bad Request"
    )


@app.router.route("/fruits", "GET")
async def get_all_products(request):
    print(f"Request: {request.method} {request.path}")
    await asyncio.sleep(5)
    return Response(
        status_code=200,
        status_message="Ok",
        headers={"Content-Type": "text/html"},
        message="<h1>All Fruits</h1><ol><li>Mango</li><li>Apple</li><li>Banana</li><li>Orange</li></ol>"
    )

@app.router.route("/bad", "GET")
def get_bad_response(request):
    print(f"Request: {request.method} {request.path}")
    return "Bad Response"


@app.router.route("/fruit", "POST")
def create_fruit(request):
    print(f"Request: {request.method} {request.path}")
    fruit = Fruit()
    if request.body:
        if request.body.get("name"):
            fruit.name = request.body.get("name")
            fruit.save()
            return Response(
                status_code=201,
                status_message="Created",
                headers={"Content-Type": "text/html"},
                message=f"{fruit} added successfully"
            )
    return Response(
        status_code=400,
        status_message="Bad Request",
        headers={"Content-Type": "text/html"},
        message="Bad Request"
    )


asyncio.run(app.start())