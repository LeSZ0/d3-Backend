import config as conf
from starlette.applications import Starlette
from typing import NoReturn
from routes import ROUTES

def startup():
    conf.Base.metadata.create_all(conf.engine, checkfirst=True)


app: Starlette = Starlette(
    debug=conf.DEBUG,
    routes=ROUTES,
    on_startup=[startup],
    on_shutdown=[]
)
