from fastapi import FastAPI
from app.api.routes import router as calculator_router
from app.core.config import settings

app = FastAPI(title=settings.app_name)

app.include_router(calculator_router)
