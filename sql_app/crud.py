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


# ユーザー登録
"""
受け取るuser引数のデータ構造はFast API側の構造になる必要がある
ユーザーを作成する構造はSQL
"""
def create_user(db: Session, user: schemas.User):
    # 主キーは自動的に決まるものなのでユーザー名を取り出す
    db_user = models.User(username=user.username)
    # addからrefreshはcreateの一連の流れ
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # 生成したインスタンスを返す
    return db_user

# 会議室登録
def create_room(db: Session, room: schemas.Room):
    db_room = models.room(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 予約登録
def create_booking(db: Session, booking: schemas.Booking):
    db_booking = models.booking(
        room_id = booking.room_id,
        user_id = booking.user_id,
        booked_num = booking.booked_num,
        start_datetime = booking.start_datetime,
        end_datetime = booking.end_datetime
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking