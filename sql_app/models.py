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

"""
ondelete:親が削除された時の処理
nullable:NULLを許容するか falseの場合は許容しない
"""
class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id", ondelete="SET NULL"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="SET NULL"), nullable=False)
    booked_num = Column(Integer)
    start_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=False)