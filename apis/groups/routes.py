from starlette.routing import Route
from .endpoints import GroupsListCreate


routes = [
    Route("/", GroupsListCreate),
]
