from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import ClassVar


class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:postgres@localhost:5432/startup'
    DBaseModel: ClassVar = declarative_base()
    TEMPLATES: ClassVar = Jinja2Templates(directory="templates")
    MEDIA: ClassVar = Path('media')

    class Config:
        case_sensitive = True



settings: Settings = Settings()

