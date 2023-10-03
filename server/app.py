from flask import Flask, jsonify, request
from flask_migrate import Migrate 

from models import db, Transaction, Investment, Investor, ProfitLoss

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(db, app)

db.init(app)

if __name__ == ('__main__'):
    with app.app_context():
        app.run(port=5555, debug=True)