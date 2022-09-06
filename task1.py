import os

import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Publisher(Base):

    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(length=40))

class Book(Base):

    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    title = sq.Column(sq.String(length=100), nullable=False, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='books')

class Shop(Base):

    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    name = sq.Column(sq.String(length=40))

class Stock(Base):

    __tablename__= 'stock'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.Integer)

    book = relationship(Book)
    shop = relationship(Shop)

class Sale(Base):

    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True, nullable=False)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'))
    count = sq.Column(sq.Integer)

    stock = relationship(Stock)


login = os.getenv('login')
password = os.getenv('password')
adress = os.getenv('adress')
db_name = os.getenv('db_name')

DSN = f'postgresql://{login}:{password}@{adress}/{db_name}'
engine = sqlalchemy.create_engine(DSN)
Base.metadata.create_all(engine)




