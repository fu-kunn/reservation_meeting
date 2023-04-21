from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, models, crud
from .database import SessionLocal, engine
# import datetime
# from pydantic import BaseModel, Field

# スキーマに移行のためコメントアウト
# class Booking(BaseModel):
#     booking_id: int
#     user_id: int
#     room_id: int
#     booked_num: int
#     start_datetime: datetime.datetime
#     end_datetime: datetime.datetime


# class User(BaseModel):
#     user_id: int
#     username: str = Field(max_length=12)


# class Room(BaseModel):
#     room_id: int
#     room_name: str = Field(max_length=12)
#     capacity: int

# SQLiteのデータベースを作成している
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# セッションを獲得するための関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/")
# async def index():
#     return {"message": "Succes"}


"""
List[]を使うことで複数のユーザー情報を取得できる
schemas.Userは1つのユーザー情報
db: Session = Depends(get_db)→get_db()関数で取得したセッションをdbに入れている
"""
# Read
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/rooms", response_model=List[schemas.Room])
async def read_rooms(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rooms = crud.get_rooms(db, skip=skip, limit=limit)
    return rooms

@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bookings = crud.get_bookings(db, skip=skip, limit=limit)
    return bookings


# Create
@app.post("/users", response_model=schemas.User)
# async def create_users(user: schemas.User, db: Session = Depends(get_db)):
async def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/rooms", response_model=schemas.Room)
async def create_rooms(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db=db, room=room)

@app.post("/bookings", response_model=schemas.Booking)
async def create_bookings(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)