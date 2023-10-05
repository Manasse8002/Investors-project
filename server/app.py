from flask import Flask, jsonify, request
from flask_migrate import Migrate 

from models import db, Transaction, Investment, Investor, ProfitLoss

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///money.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(db, app)

db.init(app)

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







    


