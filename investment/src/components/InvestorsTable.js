import React, { useEffect, useState } from "react";
import '../App.css';

function InvestorTable() {
  const [investors, setInvestors] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/investors') 
      .then(response => response.json())
      .then(data => {
        setInvestors(data);
      });
  }, []);

  return (
    <div>
      <h1>Investor List</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Email</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {investors.map(investor => (
            <tr key={investor.id}>
              <td>{investor.id}</td>
              <td>{investor.username}</td>
              <td>{investor.email}</td>
              <td>{investor.created_at}</td>
              <td>{investor.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InvestorTable;
