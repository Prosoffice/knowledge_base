from fastapi import APIRouter

from app.api.gdpr_articles.controllers import gdpr_article_controller
from app.api.case_studies.controllers import case_study_controller
from app.api.regulations.controllers import regulation_controller

api_router = APIRouter()
api_router.include_router(gdpr_article_controller.router, tags=["GDPR Articles"])
api_router.include_router(case_study_controller.router, tags=["Case Studies"])
api_router.include_router(regulation_controller.router, tags=["Regulations"])
