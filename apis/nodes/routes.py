from starlette.routing import Route
from .endpoints import NodesListCreate


routes = [
    Route("/", NodesListCreate),
]
