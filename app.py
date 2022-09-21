from datetime import date
from  flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData()
users_table = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String),
)
metadata.create_all(engine)


class Terminarz(declarative_base()):
   __tablename__ = 'zadania'

   id = Column(Integer, primary_key=True)
   name = Column(String)
   date = Column(Date)
   description = Column(String)

   def __init__(self, name, date, description):
      self.name = name
      self.date = date
      self.description = description

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/')
def hello():
   return render_template('organizer.html')

# @app.route('/organizer')
# def organizer():
#    return render_template('organizer.html')

if __name__ == '__main__':
   app.run(debug=True)
