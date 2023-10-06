import React, { useEffect, useState } from "react";
import '../App.css';
function InvestorsTable() {
  const [investors, setInvestors] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/investors') 
      .then((response) => response.json())
      .then((data) => setInvestors(data))
      .catch((error) => console.error('Error fetching investors:', error));
  }, []);

  return (
    <div className="table-container"> 
      <h2>Investors Table</h2>
      <table className="table"> 
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Address</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {investors.map((investor) => (
            <tr key={investor.id}>
              <td>{investor.id}</td>
              <td>{investor.name}</td>
              <td>{investor.email}</td>
              <td>{investor.phone}</td>
              <td>{investor.address}</td>
              <td>{investor.created_at}</td>
              <td>{investor.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InvestorsTable;
