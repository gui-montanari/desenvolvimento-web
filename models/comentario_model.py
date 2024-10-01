from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped
from core.configs import settings
from models.post_model import PostModel

class ComentarioModel(settings.DBBaseModel):
    __tablename__ = 'comentarios'
    
    id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    data: Mapped[datetime] = Column(DateTime, default=datetime.now, index=True)
    id_post: Mapped[int] = Column(Integer, ForeignKey('posts.id'))
    
    # Definindo o relacionamento com PostModel
    post: Mapped[PostModel] = relationship('PostModel', back_populates='comentarios', lazy='joined')
    
    autor: Mapped[str] = Column(String(200))
    texto: Mapped[str] = Column(String(400))
  
