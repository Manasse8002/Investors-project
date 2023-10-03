from models import db, Investment, Investor, Transaction, ProfitLoss
from faker import Faker
import random
from datetime import  timedelta
from models import db 

fake = Faker() 


def seed_database():

    Investment.query.delete()
    Investor.query.delete()
    Transaction.query.delete()
    ProfitLoss.query.delete()
    

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

        def SeedingInvestments():
            print("💸Seeding investments...")
        SeedingInvestments()


        for _ in range(random.randint(1, 7)):
            investment = Investment(
                investor_id = investor.id,
                name=fake.company(),
                amount=random.uniform(5000, 100000),
                date=fake.date_between(start_date='-2y', end_date='today')
            )
            db.session.add(investment)
        
        def SeedingInvestmentsDone():
            print("💸Seeding investments...Done!")
        SeedingInvestmentsDone()

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

        def SeedingTransactions():
            print("💸Seeding transactions...")
        SeedingTransactions()

        for _ in range(random.randint(1, 10)):
            transaction = Transaction (
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











   