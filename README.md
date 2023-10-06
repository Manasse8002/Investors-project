# Investment-project


# Description
This project is a full-stack investment application built with Flask, SQLAlchemy, and Flask-Bcrypt. It allows users to manage their investments, profit/loss records, and transactions. The application provides endpoints to create, read, update, and delete data related to investors, investments, profit/loss records, and transactions.

# Features
- Investors:

Create a new investor (POST /investors)
Update an existing investor (PATCH /investors/<investor_id>)

- Investments:

Create a new investment (POST /investments)
Update an existing investment (PATCH /investments/<investment_id>)

- Profit/Loss Records:

Create a new profit/loss record (POST /profit-loss)
Update an existing profit/loss record (PATCH /profit-loss/<record_id>)

- Transactions:

Create a new transaction (POST /transactions)
Update an existing transaction (PATCH /transactions/<transaction_id>)

# Data Retrieval:

Retrieve all investors (GET /investors)
Retrieve all investments (GET /investments)
Retrieve all profit/loss records (GET /profit-loss)
Retrieve all transactions (GET /transactions)

# Installation
- Clone the repository:
Copy code
git clone <https://github.com/Manasse8002/Investors-project>
cd investment-application

- Install dependencies:
pip install -r requirements.txt

- Set up the database:
flask db init
flask db migrate
flask db upgrade

- Run the application:
flask run

# Usage
- Create a new investor:

Endpoint: POST /investors
Payload:
json
Copy code
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123"
}

- Update an existing investor:

Endpoint: PATCH /investors/<investor_id>
Payload:
json
Copy code
{
    "username": "new_username",
    "email": "new_email@example.com"
}

- Create a new investment:

Endpoint: POST /investments
Payload:
json
Copy code
{
    "investor_id": 1,
    "name": "Company ABC",
    "amount": 5000.00,
    "date": "2023-10-10"
}

- Update an existing investment:

Endpoint: PATCH /investments/<investment_id>
Payload:
json
Copy code
{
    "name": "New Company Name",
    "amount": 6000.00,
    "date": "2023-11-01"
}

- Create a new profit/loss record:

Endpoint: POST /profit-loss
Payload:
json
Copy code
{
    "investment_id": 1,
    "amount": 200.00,
    "transaction_date": "2023-10-20"
}

- Update an existing profit/loss record:

Endpoint: PATCH /profit-loss/<record_id>
Payload:
json
Copy code
{
    "amount": 250.00,
    "transaction_date": "2023-11-05"
}

- Create a new transaction:

Endpoint: POST /transactions
Payload:
json
Copy code
{
    "investment_id": 1,
    "transaction_type": "buy",
    "transaction_amount": 1000.00,
    "transaction_units": 5.0,
    "transaction_date": "2023-10-15"
}

- Update an existing transaction:

Endpoint: PATCH /transactions/<transaction_id>
Payload:
json
Copy code
{
    "transaction_type": "sell",
    "transaction_amount": 1500.00,
    "transaction_units": 3.0,
    "transaction_date": "2023-10-25"
}

# Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

# License
This project is licensed under the MIT License.



