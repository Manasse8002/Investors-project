import { useEffect, useState } from "react";
import '../App.css';

function InvestmentsTable() {
  const [investments, setInvestments] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555')
      .then((response) => response.json())
      .then((data) => setInvestments(data))
      .catch((error) => console.error('Error fetching investments:', error));
  }, []);

  return (
    <div>
      <h2>Investments Table</h2>
      <table className="common-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Investor ID</th>
            <th>Investment Amount</th>
            <th>Investment Date</th>
            <th>Investment Type</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {investments.map((investment) => (
            <tr key={investment.id}>
              <td>{investment.id}</td>
              <td>{investment.investor_id}</td>
              <td>{investment.investment_amount}</td>
              <td>{investment.investment_date}</td>
              <td>{investment.investment_type}</td>
              <td>{investment.created_at}</td>
              <td>{investment.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default InvestmentsTable;
