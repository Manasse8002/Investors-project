from flask import Flask, jsonify, request
from models import db, Transaction, Investment, Investor, ProfitLoss
from flask_migrate import Migrate 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

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

if __name__ == '__main__':
    with app.app_context():
        app.run(port=5555, debug=True)
<<<<<<< HEAD
         
=======







    


>>>>>>> bf4463e (committing changes in Investors-project)
