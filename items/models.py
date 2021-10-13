import datetime

from sqlalchemy import Column, Integer, String

from core.database import Base


class Item(Base):
    """ Item model """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, unique=True)
    value = Column(
        String,
    )
    timestamp = Column(
        Integer,
        default=int(datetime.datetime.now().timestamp()),
    )
