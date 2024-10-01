from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship
from core.configs import settings
from models.area_model import AreaModel

class DuvidaModel(settings.DBBaseModel):
    __tablename__: str = 'duvida'
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    id_area: Mapped[int] = Column(Integer, ForeignKey('areas.id'))
    area: Mapped[AreaModel] = relationship('AreaModel', lazy='joined')
    titulo: Mapped[str] = Column(String(200))
    resposta: Mapped[str] = Column(String(400))
    

