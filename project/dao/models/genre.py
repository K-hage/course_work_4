from sqlalchemy import Column, String

from project.setup.db import models


class Genre(models.Base):
    """ Модель жанра """

    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)
