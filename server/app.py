import sys
import os
from flask import Flask, jsonify, request
from models import db, Transaction, Investment, Investor, ProfitLoss
from flask_migrate import Migrate 
import bcrypt
from flask_cors import CORS
import random
from datetime import timedelta


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

@app.route('/investors', methods=['GET'])
def get_investors():
    investors = Investor.query.all()
    investor_list = [{'id': investor.id, 'username': investor.username, 'email': investor.email} for investor in investors]

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

app_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.append(app_directory)

@app.route('/investors', methods=['GET'])
def get_investors():
    investors = Investor.query.all()
    investor_list = [{'id': investor.id, 'username': investor.username, 'email': investor.email, 'created_at': investor.created_at, 'updated_at': investor.updated_at} for investor in investors]

    return jsonify(investor_list)

@app.route('/investments', methods=['GET'])
def get_investments():
    investments = Investment.query.all()
    investment_list = [{'id':investment.id, 'name': investment.name, 'amount': investment.amount, 'date':investment.date.strftime('%Y-%m-%d')} for investment in investments]
    return jsonify(investment_list)

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()

    transaction_list = [{'id': transaction.id, 'investment_id': transaction.investment.id, 'type': transaction.transaction_type, 'amount': transaction.amount, 'units': transaction.transaction_units, 'date': transaction.transaction_date.strftime('%Y-%m-%d')} for transaction in transactions]

    return jsonify(transaction_list)

@app.route('/profit-loss', methods=['GET'])
def get_profit_loss():
    profit_loss_records = ProfitLoss.query.all()

    profit_loss_list = [{'id': record.id, 'investment_id': record.investment_id, 'amount': record.profit_or_loss_amount, 'date':record.transcation_date.strftime('%Y-%m-%d')} for record in profit_loss_records]
    return jsonify(profit_loss_list)

@app.route('/invest', methods=['GET'])
def investor():
    return jsonify(investor)

# Seeding the database
@app.route('/seed-database', methods=['GET'])
def seed_database():
    # Import necessary modules from seed.py
    from seed import fake

    # Clear existing data
    Investment.query.delete()
    Investor.query.delete()
    Transaction.query.delete()
    ProfitLoss.query.delete()

    # Seed Investors
    def SeedingInvestors():
        print("💸Seeding investors...")

    SeedingInvestors()

    for _ in range(30):
        investor = Investor(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
        )
        db.session.add(investor)

    def SeedingInvestorsDone():
        print("💸Seeding investors...Done!")

    SeedingInvestorsDone()

    # Seed Investments
    def SeedingInvestments():
        print("💸Seeding investments...")

    SeedingInvestments()

    for _ in range(random.randint(1, 7)):
        investment = Investment(
            investor_id=investor.id,
            name=fake.company(),
            amount=random.uniform(5000, 100000),
            date=fake.date_between(start_date='-2y', end_date='today')
        )
        db.session.add(investment)

    def SeedingInvestmentsDone():
        print("💸Seeding investments...Done!")

    SeedingInvestmentsDone()

    # Seed Profit/Loss
    def SeedingProfitLoss():
        print("💸Seeding profit/loss...")

    SeedingProfitLoss()

    profit_loss = ProfitLoss(
        investment_id=investment.id,
        profit_loss_amount=random.uniform(-15000, 250000),
        transaction_date=investment.date + timedelta(days=random.randint(1, 365))
    )
    db.session.add(profit_loss)

    def SeedingProfitLossDone():
        print("💸Seeding profit/loss...Done!")

    SeedingProfitLossDone()

    # Seed Transactions
    def SeedingTransactions():
        print("💸Seeding transactions...")

    SeedingTransactions()

    for _ in range(random.randint(1, 10)):
        transaction = Transaction(
            investment_id=investment.id,
            transaction_type=random.choice(['buy', 'sell']),
            transaction_date=investment.date + timedelta(days=random.randint(1, 365)),
            transaction_amount=random.uniform(1500, 150000),
            transaction_units=random.uniform(1, 100)
        )
        db.session.add(transaction)

    def SeedingTransactionsDone():
        print("💸Seeding transactions...Done!")

    SeedingTransactionsDone()

    db.session.commit()

    def SeedingDone():
        print("💸Seeding...Done!")

    SeedingDone()

    return jsonify(message='Database seeded successfully')


@app.route('/investors', methods=['POST'])
def create_investor():
    data =  request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')  # Corrected to get the password from the JSON data

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_investor = Investor(username=username, email=email, password_hash=hashed_password)
    db.session.add(new_investor)
    db.session.commit()

    return jsonify(message='Investor created successfully'), 201

@app.route('/investors/<int:investor_id>', methods=['PATCH'])
def update_investor(investor_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    investor = Investor.query.get(investor_id)
    if not investor:
        return jsonify(message='Investor not found'), 404
    
    investor.username = username
    investor.email = email
    db.session.commit()

    return jsonify(message='Investor updated successfully!')

@app.route('/investments', methods=['POST'])
def create_investment():
    data = request.get_json()
    investor_id = data.get('investor_id')
    name = data.get('name')
    amount = data.get('amount')
    date = data.get('date')

    new_investment = Investment(investor_id=investor_id, name=name, amount=amount, date=date)
    db.session.add(new_investment)
    db.session.commit()

    return jsonify(message='Investment created successfully!'), 201

@app.route('/investments/<int:investment_id>', methods=['PATCH'])
def update_investment(investment_id):
    data = request.get_json()
    name = data.get('name')
    amount = data.get('amount')
    date = data.get('date')

    investment = Investment.query.get(investment_id)
    if not investment:
        return jsonify(message='Investment not found'), 404
    
    investment.name = name
    investment.amount = amount
    investment.date = date
    db.session.commit()

    return jsonify(message='Investment updated successfully!')

@app.route('/profit-loss', methods=['POST'])
def create_profit_loss():
    data = request.get_json()
    investment_id = data.get('investment_id')
    amount = data.get('amount')
    transaction_date = data.get('transaction_date')

    new_profit_loss = ProfitLoss(investment_id=investment_id, profit_loss_amount=amount, transaction_date=transaction_date)
    db.session.add(new_profit_loss)
    db.session.commit()

    return jsonify(message='Profit/Loss record created successfully!'), 201

@app.route('/profit-loss/<int:record_id>', methods=['PATCH'])
def update_profit_loss(record_id):
    data = request.get_json()
    amount = data.get('amount')
    transaction_date = data.get('transaction_date')

    record = ProfitLoss.query.get(record_id)
    if not record:
        return jsonify(message='Profit/Loss record not found!'), 404
    
    record.profit_loss_amount = amount
    record.transaction_date = transaction_date
    db.session.commit()

    return jsonify(message='Profit/Loss record updated successfully!')

@app.route('/transactions', methods=['POST'])
def create_transaction():
    data = request.get_json()
    investment_id = data.get('investment_id')
    transaction_type = data.get('transaction_type')
    transaction_amount = data.get('transaction_amount')
    transaction_units = data.get('transaction_units')
    transaction_date = data.get('transaction_date')

    new_transaction = Transaction(investment_id=investment_id, transaction_type=transaction_type, transaction_amount=transaction_amount, transaction_units=transaction_units, transaction_date=transaction_date)

    db.session.add(new_transaction)
    db.session.commit()

    return jsonify(message='Transaction created successfully!'), 201

@app.route('/transactions/<int:transaction_id>', methods=['PATCH'])
def update_transaction(transaction_id):
    data = request.get_json()
    transaction_type = data.get('transaction_type')
    transaction_amount = data.get('transaction_amount')
    transaction_units = data.get('transaction_units')
    transaction_date = data.get('transaction_date')

    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify(message='Transaction not found'), 404
    
    transaction.transaction_type = transaction_type
    transaction.transaction_amount = transaction_amount
    transaction.transaction_units = transaction_units
    transaction.transaction_date = transaction_date
    db.session.commit()

    return jsonify(message='Transaction updated successfully!')


if __name__ == '__main__':
    with app.app_context():
        app.run(port=5555, debug=True)








    



