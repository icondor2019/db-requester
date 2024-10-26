from fastapi import APIRouter

from app.controllers import (
    health_controller,
    db_requester_controller
)

api_router = APIRouter()
api_router.include_router(health_controller.api)
api_router.include_router(db_requester_controller.api)
