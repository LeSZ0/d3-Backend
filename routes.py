from starlette.routing import Route, Mount
from starlette.responses import JSONResponse
from apis.groups.routes import routes as group_routes
from apis.nodes.routes import routes as node_routes
from apis.links.routes import routes as link_routes
from apis.core.endpoints import Miserables


ROUTES = [
    Route('/', Miserables),
    Mount('/groups', routes=group_routes),
    Mount('/nodes', routes=node_routes),
    Mount('/links', routes=link_routes),
]
