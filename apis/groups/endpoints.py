from starlette.responses import JSONResponse
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from models import Group
from config import session
from interfaces import GroupInterface
import json


class GroupsListCreate(HTTPEndpoint):
    async def get(self, request: Request) -> JSONResponse:
        """Endpoint to list all groups"""
        groups: list[Group] = session.query(Group).all()
        return JSONResponse([g.serialize() for g in groups])

    async def post(self, request: Request) -> JSONResponse:
        """Endpoint to create a group"""
        request_data = await request.json()
        try:
            pre_group: GroupInterface = GroupInterface(**request_data)

        except TypeError as e:
            return JSONResponse({"error": str(e)}, status_code=400)

        group: Group = Group(**request_data)
        session.add(group)
        session.commit()

        return JSONResponse(group.serialize())
