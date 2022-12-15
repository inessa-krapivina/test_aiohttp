import aiohttp
import logging


async def on_request_start(session, context, params):
    logging.getLogger("aiohttp.client").debug(f"Starting request <{params}>")


async def auth(login: str, passwd: str):
    logging.basicConfig(level=logging.DEBUG)
    trace_config = aiohttp.TraceConfig()
    trace_config.on_request_start.append(on_request_start)

    async with aiohttp.ClientSession(trace_configs=[trace_config]) as session:
        async with session.post(
            "http://127.0.0.1:8080/auth", data={"login": login, "passwd": passwd}
        ) as response:

            html = await response.text()
            print(response.text)


async def create_user(
    name: str, lastname: str, login: str, passwd: str, date_of_birth: str
):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://127.0.0.1:8080/create",
            data={
                "name": name,
                "lastname": lastname,
                "login": login,
                "passwd": passwd,
                "date_of_birth": date_of_birth,
            },
        ) as response:

            html = await response.text()
            print(response.text)


async def read_all_users(
    name: str, lastname: str, login: str, passwd: str, date_of_birth: str
):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://127.0.0.1:8080/read",
            data={
                "name": name,
                "lastname": lastname,
                "login": login,
                "passwd": passwd,
                "date_of_birth": date_of_birth,
            },
        ) as response:

            html = await response.text()
            print(response.text)


async def update_name(old_name: str, new_name: str):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://127.0.0.1:8080/updateName",
            data={"old_name": old_name, "new_name": new_name},
        ) as response:

            html = await response.text()


async def delete_user(
    name: str, lastname: str, login: str, passwd: str, date_of_birth: str
):
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "http://127.0.0.1:8080/delete",
            data={
                "name": name,
                "lastname": lastname,
                "login": login,
                "passwd": passwd,
                "date_of_birth": date_of_birth,
            },
        ) as response:

            html = await response.text()
            print(response.text)
