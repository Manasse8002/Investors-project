import { useEffect, useState } from "react";
function ProfitTable() {
  const [profits, setProfits] = useState([]);

  useEffect(() => {
    
    fetch('')
      .then((response) => response.json())
      .then((data) => setProfits(data))
      .catch((error) => console.error('Error fetching profits:', error));
  }, []);

  return (
    <div>
      <h2>Profit Table</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Investment ID</th>
            <th>Profit Amount</th>
            <th>Profit Date</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {profits.map((profit) => (
            <tr key={profit.id}>
              <td>{profit.id}</td>
              <td>{profit.investment_id}</td>
              <td>{profit.profit_amount}</td>
              <td>{profit.profit_date}</td>
              <td>{profit.created_at}</td>
              <td>{profit.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProfitTable;
