from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from models import Node, Group
from config import session
from interfaces import NodeInterface


class NodesListCreate(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        """Endpoint to list all nodes"""
        nodes: list[Nodes] = session.query(Node).all()
        return JSONResponse([node.serialize() for node in nodes])

    async def post(self, request: Request) -> JSONResponse:
        """Endpoint to create a node"""
        request_data = await request.json()
        try:
            node_iface = NodeInterface(**request_data)

        except TypeError as e:
            return JSONResponse({"error": str(e)}, status_code=400)

        node: Node = Node(**request_data)
        session.add(node)
        session.commit()

        return JSONResponse(node.serialize(), status_code=201)
