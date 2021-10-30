from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from models import Node, Link
from config import session


class Miserables(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        """Endpoint to list all nodes and links"""
        nodes: list[Node] = session.query(Node).all()
        links: list[Link] = session.query(Link).all()
        miserables: dict = {
            "nodes": [node.serialize() for node in nodes],
            "links": [link.serialize() for link in links]
        }
        return JSONResponse(miserables, status_code=200)
