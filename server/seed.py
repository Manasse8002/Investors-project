from models import db, Investment, Investor, Transaction, ProfitLoss
from faker import Faker
import random
from datetime import  timedelta
from app import app 

fake = Faker() 


def seed_database():
 with app.app_context():

    Investment.query.delete()
    Investor.query.delete()
    Transaction.query.delete()
    ProfitLoss.query.delete()
    

    def SeedingInvestors():
        print("💸Seeding investors...")
    SeedingInvestors()

    investor = Investor(
            username=fake.user_name(),
            email=fake.email(),
            password=fake.password(),
    )
    db.session.add(investor)

    investment = Investment(
                investor_id = investor.id,
                name=fake.company(),
                amount=random.uniform(5000, 100000),
                date=fake.date_between(start_date='-2y', end_date='today')
    )
    db.session.add(investment)

    

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
       
   
<<<<<<< HEAD
    with db.session.begin() as session:
     for _ in range(random.randint(1, 10)):
        try:
          if investment.id is not None:
=======
 
        # if investment.id is not None:
        for _ in range(random.randint(1, 10)):
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
            transaction = Transaction (
                investment_id=investment.id,
                transaction_type=random.choice(['buy', 'sell']),
                transaction_date=investment.date + timedelta(days=random.randint(1, 365)),
                transaction_amount=random.uniform(1500, 150000),
                transaction_units=random.uniform(1, 100)
            )
<<<<<<< HEAD
            session.add(transaction)
          else:
            print("Invalid investment ID:", investment.id)

        except Exception as e:
            print("Error adding transaction:", e)
            session.rollback()
=======
            db.session.add(transaction)
        # else:
        #     print("Invalid investment ID:", investment.id)
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42

            def SeedingTransactionsDone():
             print("💸Seeding transactions...Done!")
             SeedingTransactionsDone()

    db.session.commit()
<<<<<<< HEAD

if __name__ == "__main__":
    seed_database()

=======
>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42

def SeedingDone():
    print("💸Seeding...Done!")

if __name__ == "__main__":
    seed_database()
    SeedingDone()













<<<<<<< HEAD
=======



>>>>>>> 231d69d0ecf34e92c8df8f08afa0d8c5d909db42
   