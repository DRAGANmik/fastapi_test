from fastapi import APIRouter

from items import routes as items_routers

routes = APIRouter()

routes.include_router(items_routers.router, prefix="/items")
