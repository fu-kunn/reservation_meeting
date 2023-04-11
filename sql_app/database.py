# 外部ライブラリを読み込む時には空ファイル（__init__.py）が必要

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# データベースのファイルを明示している
# 今回はデータベースサーバーを用いるわけではない
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# SQLiteのみに必要な引数（他のデータベースでは必要ない）
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# 既存であるクラスを継承してデータの構造を作るもの
Base = declarative_base()