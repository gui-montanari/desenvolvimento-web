from typing import List
from datetime import datetime

import sqlalchemy.orm as orm

from core.configs import settings
from models.tag_model import TagModel
from models.autor_model import AutorModel
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey


# Tabela de associação para relacionamento muitos-para-muitos entre Post e Tag
tags_post = Table(
    'tags_post',
    settings.DBBaseModel.metadata,
    Column('id_post', Integer, ForeignKey('posts.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)

# Tabela de associação para relacionamento muitos-para-muitos entre Post e Comentário
comentarios_post = Table(
    'comentarios_post',
    settings.DBBaseModel.metadata,
    Column('id_post', Integer, ForeignKey('posts.id')),
    Column('id_comentario', Integer, ForeignKey('comentarios.id'))
)


class PostModel(settings.DBBaseModel):
    """Posts do blog"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    data = Column(DateTime, default=datetime.now, index=True)
    # Um Post pode ter várias tags
    tags = relationship('TagModel', secondary='tags_post', backref='tagp', lazy='joined')
    imagem = Column(String(100))  # 900x400
    texto = Column(String(1000), nullable=False)
    # Um Post pode ter vários comentários
    comentarios = relationship('ComentarioModel', secondary='comentarios_post', backref='comentario', lazy='joined')
    id_autor = Column(Integer, ForeignKey('autores.id'), nullable=False)
    autor = relationship('AutorModel', lazy='joined')

