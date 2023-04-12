from sqlalchemy.orm import Session
# 同じフォルダ内のmodel.pyとshemas.pyを呼び出している
from . import models, schemas


# ユーザー一覧の取得
"""
db: Session →必要なんだなぐらいに思っておく
skip: int = 0→ユーザー一覧を取得するときに上位何件をスキップするのか（今回は上位から全て取得）
limit: int = 100 →最大で100件取得する
"""
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# 会議室一覧の取得
def get_rooms(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()


# 予約一覧の取得
def get_bookings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Booking).offset(skip).limit(limit).all()