from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import dotenv

# Загрузка переменных окружения из .env-файла
dotenv.load_dotenv()

DATABASE_URL = (f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
                f"@localhost:5432/{os.getenv('POSTGRES_NAME')}")

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Создание подключения к базе данных
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()
