from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, Session
from sqlalchemy.future import select


sele = select

engine = create_engine("sqlite:///banco.db", echo=True)
session = Session(engine, future=True)
Base = declarative_base()

class Pergunta(Base):
    __tablename__ = "pergunte"
    id = Column(Integer, primary_key=True)
    pergunta = Column(String(1000), nullable=False)
    opicoes = Column(String, nullable=False)
    resposta = Column(String, nullable=False)

Base.metadata.create_all(engine)