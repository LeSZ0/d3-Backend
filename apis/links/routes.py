from starlette.routing import Route
from .endpoints import LinksListCreate


routes = [
    Route("/", LinksListCreate),
]