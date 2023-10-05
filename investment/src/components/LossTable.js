import { useEffect, useState } from "react";
function LossesTable() {
  const [losses, setLosses] = useState([]);

  useEffect(() => {
    
    fetch('')
      .then((response) => response.json())
      .then((data) => setLosses(data))
      .catch((error) => console.error('Error fetching losses:', error));
  }, []);

  return (
    <div>
      <h2>Losses Table</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Investment ID</th>
            <th>Loss Amount</th>
            <th>Loss Date</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {losses.map((loss) => (
            <tr key={loss.id}>
              <td>{loss.id}</td>
              <td>{loss.investment_id}</td>
              <td>{loss.loss_amount}</td>
              <td>{loss.loss_date}</td>
              <td>{loss.created_at}</td>
              <td>{loss.updated_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default LossesTable;
