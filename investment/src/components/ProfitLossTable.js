import React, { useEffect, useState } from "react";
import '../App.css';

function ProfitLossTable() {
  const [profitLoss, setProfitLoss] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/profit-loss') 
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setProfitLoss(data);
      })
      .catch(error => {
        setError(error);
      });
  }, []);

  if (error) {
    return (
      <div>
        <h1>Error</h1>
        <p>{error.message}</p>
      </div>
    );
  }

  return (
    <div>
      <h1>Profit/Loss List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Investment ID</th>
            <th>Investor ID</th>
            <th>Profit/Loss Amount</th>
            <th>Transaction Date</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {profitLoss.map(record => (
            <tr key={record.id}>
              <td>{record.id}</td>
              <td>{record.investment_id}</td>
              <td>{record.investor_id}</td>
              <td>{record.profit_loss_amount}</td>
              <td>{record.transaction_date}</td>
              <td>{record.created_at}</td>
              <td>{record.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProfitLossTable;
