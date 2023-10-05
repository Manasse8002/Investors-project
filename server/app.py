from flask import Flask, jsonify, request
from flask_migrate import Migrate 

from models import db, Transaction, Investment, Investor, ProfitLoss

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(db, app)

db.init(app)

@app.route('/investors', methods=['GET'])
def get_investors():
    investors = Investor.query.all()
    investor_list = [{'id': investor.id, 'username': investor.username, 'email': investor.email} for investor in investors]
    return jsonify(investor_list)

@app.route('/investments', methods=['GET'])
def get_investments():
    investments = Investment.query.all()
    investment_list = [{'id':investment.id, 'name': investment.name, 'amount': investment.amount, 'date':investment.date.strftime('%Y-%m-%d')} for investment in investments]
    return jsonify(investment_list)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    transaction_list = [{'id': transaction.id, 'investment_id': transaction.investment.id, 'type': transaction.transaction_type, 'amount': transaction.amount, 'units': transaction.transaction_units, 'date': transaction.transaction_date_strftime('%Y-%m-%d')} for transaction in transactions]
    return jsonify(transaction_list)

@app.route('/profit-loss', methods=['GET'])
def get_profit_loss():
    profit_loss_records = ProfitLoss.query.all()
    profit_loss_list = [{'id': record.id, 'investment_id': record.investment_id, 'amount': record.profit_or_loss_amount, 'date':record.transcation_date.strftime('%Y-%m-%d')} for record in profit_loss_records]
    return jsonify(profit_loss_list)

if __name__ == ('__main__'):
    with app.app_context():
        app.run(port=5555, debug=True)
         