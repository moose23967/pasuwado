from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from uvicorn import run as uvicorn_run

from .modules.english_words_dictionary import EnglishWordsDictionary
from .modules.random_number_generator import RandomNumberGenerator
from .modules.random_password_generator import RandomPasswordGenerator

templates = Jinja2Templates("pasuwado/templates")

random_password_generator = RandomPasswordGenerator(
    EnglishWordsDictionary(), random_number_generator=RandomNumberGenerator()
)


async def homepage(request: Request):
    password = random_password_generator.generate(5)

    return templates.TemplateResponse(
        "index.html", context={"request": request, "password": password}
    )


routes = [
    Route("/", homepage),
    Mount("/static", app=StaticFiles(directory="pasuwado/static"), name="static"),
]

app = Starlette(routes=routes)

uvicorn_run(app)
