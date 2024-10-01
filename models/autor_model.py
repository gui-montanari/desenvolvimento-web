from typing import List
import sqlalchemy.orm as orm
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from core.configs import settings
from models.tag_model import TagModel

# Many-to-many relationship table
tags_autor = Table(
    'tags_autor',
    settings.DBBaseModel.metadata,
    Column('id_autor', Integer, ForeignKey('autores.id')),
    Column('id_tag', Integer, ForeignKey('tags.id'))
)

class AutorModel(settings.DBBaseModel):
    """Autor das postagens no blog"""
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    imagem = Column(String(100))  # 40x40
    # Relationship to TagModel
    tags = orm.relationship('TagModel', secondary=tags_autor, backref='authors', lazy='joined')



