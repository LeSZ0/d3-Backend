from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from models import Link
from config import session
from interfaces import LinkInterface


class LinksListCreate(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        """Endpoint to list all links"""
        links: list[Link] = session.query(Link).all()
        return JSONResponse([link.serialize() for link in links])

    async def post(self, request: Request) -> JSONResponse:
        """Endpoint to create a link"""
        request_data = await request.json()

        try:
            link_iface = LinkInterface(**request_data)

        except TypeError as e:
            return JSONResponse({"error": str(e)}, status_code=400)

        link: Link = Link(**request_data)
        session.add(link)
        session.commit()

        return JSONResponse(link.serialize(), status_code=201)
