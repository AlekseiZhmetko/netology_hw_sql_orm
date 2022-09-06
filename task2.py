import os
import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import json

from task1 import Publisher, Shop, Book, Stock, Sale

login = os.getenv('login')
password = os.getenv('password')
adress = os.getenv('adress')
db_name = os.getenv('db_name')

DSN = f'postgresql://{login}:{password}@{adress}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

    for record in data:
        model = {
            'publisher': Publisher,
            'shop': Shop,
            'book': Book,
            'stock': Stock,
            'sale': Sale,
        }[record.get('model')]
        session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

pub = input('Введите id или название издателя: ')
if pub.isnumeric():
    a = session.query(Publisher).filter(Publisher.id == f'{pub}')
    for s in a.all():
        print(s.id, s.name)
else:
    a = session.query(Publisher).filter(Publisher.name.like(f'%{pub}%'))
    for s in a.all():
        print(s.id, s.name)

# a = session.query(Publisher).filter(or_(Publisher.id == f'{pub_id}', Publisher.name == f'{pub}'))
# for s in a.all():
#     print(s.id, s.name)
## в таком виде ввод в виде строки не проходит проверку на условие того, что id - int