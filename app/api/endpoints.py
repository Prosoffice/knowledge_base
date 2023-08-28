from fastapi import APIRouter

from app.api.gdpr_articles.controllers import gdpr_article_controller


api_router = APIRouter()
api_router.include_router(gdpr_article_controller.router, tags=["GDPR Articles"])
