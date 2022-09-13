import os
import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json

from task1 import Publisher, Shop, Book, Stock, Sale

login = os.getenv('login')
password = os.getenv('password')
address = os.getenv('address')
db_name = os.getenv('db_name')

DSN = f'postgresql://{login}:{password}@{address}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

# with open('fixtures/tests_data.json', 'r') as fd:
#     data = json.load(fd)
#
#     for record in data:
#         model = {
#             'publisher': Publisher,
#             'shop': Shop,
#             'book': Book,
#             'stock': Stock,
#             'sale': Sale,
#         }[record.get('model')]
#         session.add(model(id=record.get('pk'), **record.get('fields')))
# session.commit()

if __name__ == '__main__':

# чтобы выводилось название издательства и его id:

    pub = input('Введите id или название издателя: ')
    if pub.isnumeric():
        a = session.query(Publisher).filter(Publisher.id == f'{pub}')
        for s in a.all():
            print(s.id, s.name)
    else:
        a = session.query(Publisher).filter(Publisher.name.like(f'%{pub}%'))
        for s in a.all():
            print(s.id, s.name)

# чтобы выводились названия книг издательства:

    pub = input('Введите id или название издателя, книги которого нужно вывести: ')
    if pub.isnumeric():
        a = session.query(Publisher.id, Publisher.name, Book.title, Book.id).join(Book).filter(Publisher.id == f'{pub}')
        for s in a.all():
            print(s.name, '|', s.title)
    else:
        a = session.query(Publisher.id, Publisher.name, Book.title, Book.id).join(Book).filter(Publisher.name.like(f'%{pub}%'))
        for s in a.all():
            print(s.name, '|', s.title)
