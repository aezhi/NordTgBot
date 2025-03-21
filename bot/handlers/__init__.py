from aiogram import Router

from .user import user_router
from .admin import admin_router
from .system import system_router

main_router = Router()
main_router.include_routers(system_router, admin_router, user_router)

__all__ = ['main_router']
