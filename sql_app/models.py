# データベースの構造・中身

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
# database.pyからBaseを読み込む
from .database import Base

class User(Base):
    # テーブル名
    __tablename__ = "users"
    # カラム名
    # indexは検索を早くする仕組み
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)


class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    room_name = Column(String, unique=True, index=True)
    capacity = Column(Integer)