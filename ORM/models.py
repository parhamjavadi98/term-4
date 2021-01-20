from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from connection import Connection

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    studentId = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50))
    family = Column(String(50))
    grade = Column(Integer())
    created_at = Column(DateTime())

    def __init__(self, name=None, family=None, grade=None):
        self.name = name
        self.family= family
        self.grade = grade


engine = Connection().get_connection()
Base.metadate.create_all(engine, checkfirst=True)
print('Database Created!')