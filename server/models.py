from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy import MetaData
from sqlalchemy.orm import validates 


metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

db = SQLAlchemy(metadata=metadata)


class Investor(db.Model):
     __tablename__ = 'investors'

     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String, nullable=False, unique=True)
     email = db.Column(db.String, unique= True, nullable=False)
     password_hash = db.Column(db.String, nullable=False)
     created_at =  db.Column(db.DateTime, default=datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

     investments = db.relationship('Investment', backref='investor', lazy=True)
     profit_loss_records = db.relationship('ProfitLoss', backref='investor', lazy=True)

     def __init__(self, username, email, password):
          self.username = username
          self.email = email
          self.password_hash = generate_password_hash(password, method='sha256')
    
     def check_password(self, password):
          return check_password_hash(self.password_hash, password)
     
class Investment(db.Model):
     __tablename__ = 'investments'

     id = db.Column(db.Integer, primary_key=True)
     investor_id = db.Column(db.Integer, db.ForeignKey('investors.id'))
     name = db.Column(db.String, nullable=False)
     amount = db.Column(db.Float, nullable= False)
     date = db.Column(db.Date)
     created_at =  db.Column(db.DateTime, default=datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

     profit_loss_record = db.relationship('ProfitLoss', backref='investment', uselist=False)

     

class ProfitLoss (db.Model):
     __tablename__ = 'profitandloss'

     id = db.Column(db.Integer, primary_key=True)
     investment_id = db.Column(db.Integer, db.ForeignKey('investments.id'))
     profit_loss_amount = db.Column(db.Float)
     transaction_date = db.Column(db.Date)
     created_at =  db.Column(db.DateTime, default=datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Transaction(db.Model):
     
     __tablename__ = 'transaction'

     id = db.Column(db.Integer, primary_key=True)
     investment_id = db.Column(db.Integer, db.ForeignKey('investments.id'), nullable=False)
     transaction_type = db.Column(db.String(10), nullable=False) # We can add a choice here; Buy or Sell.
     transaction_date = db.Column(db.Date, nullable=False)
     transaction_amount = db.Column(db.Float, nullable=False)
     transaction_units = db.Column(db.Float) # For investments like stocks or crytpocurrencies. Not sure qhat to do with this one though. @Lavenia can step in here.
     created_at =  db.Column(db.DateTime, default=datetime.utcnow)
     updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

     investment = db.relationship('Investment', backref='transactions', lazy=True)

     @validates('transaction_type')
     def validate_transaction_type(self, key, value):
          if value not in ['buy', 'sell']:
               raise ValueError("Transaction type should be one of: 'buy', 'sell'")
          return value





