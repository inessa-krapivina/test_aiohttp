from aiohttp import web
from aiohttp_swagger import *
from sqlalchemy import and_


from src.db import Users, db_session, update_user_in_db

app = web.Application()


async def auth(request):
    data = await request.post()

    with db_session() as db:
        user = (
            db.query(Users)
            .where(and_(Users.login == data["login"], Users.passwd == data["passwd"]))
            .all()
        )

    if data["login"] == "admin" and data["passwd" == "admin"]:
        pass


async def create_user(request):
    with db_session() as db:
        data = await request.post()
        name = data["name"]
        lastname = data["lastname"]
        login = data["login"]
        passwd = data["passwd"]
        date_of_birth = data["date_of_birth"]

    return web.Response(text=str(""))


async def read_all_users(request):
    users_result = []
    with db_session() as db:
        users_result = db.query(Users).all()
        return web.Response(text=str(users_result))


async def update_user(request):
    data = await request.post()
    old_name = data["old_name"]
    new_name = data["new_name"]
    update_user_in_db(old_name=old_name, new_name=new_name)

    return web.Response(text="OK")


async def delete_user(request):
    with db_session() as db:
        data = await request.get()
        name = data["name"]
        # delete_user(name)

    return web.Response(text=str(""))


app.router.add_route("POST", "/auth", auth)
app.router.add_route("POST", "/create", create_user)
app.router.add_route("GET", "/read", read_all_users)
app.router.add_route("POST", "/updateName", update_user)
app.router.add_route("GET", "/delete", delete_user)

setup_swagger(app)

web.run_app(app, host="127.0.0.1")
