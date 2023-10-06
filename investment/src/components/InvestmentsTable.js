import React, { useEffect, useState } from "react";
import '../App.css';

function InvestmentTable() {
  const [investments, setInvestments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Update the URL to match your Flask server
    fetch('http://localhost:5555/investments')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setInvestments(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>Investment List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Amount</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {investments.map(investment => (
            <tr key={investment.id}>
              <td>{investment.id}</td>
              <td>{investment.name}</td>
              <td>{investment.amount}</td>
              <td>{investment.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InvestmentTable;
