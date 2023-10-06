import React, { useEffect, useState } from "react";
import '../App.css';


function ProfitLossTable() {
  const [data, setData] = useState([]);
  const [tableType, setTableType] = useState("");

  useEffect(() => {
    fetch('http://127.0.0.1:5555') 
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error(`Error fetching ${tableType}:`, error));
  }, [tableType]);

  const columns = {
    profit: [
      "ID",
      "Investment ID",
      "Profit Amount",
      "Profit Date",
      "Created At",
      "Updated At",
    ],
    loss: [
      "ID",
      "Investment ID",
      "Loss Amount",
      "Loss Date",
      "Created At",
      "Updated At",
    ],
  };

  const tableHeaders = columns[tableType] || [];

  return (
    <div className="profit-loss-table-container">
      <h2>{`${tableType.charAt(0).toUpperCase() + tableType.slice(1)} Table`}</h2>
      <button className="profit-loss-button" onClick={() => setTableType("profit")}>Show Profit</button>
      <button className="profit-loss-button" onClick={() => setTableType("loss")}>Show Loss</button>
      <table className="profit-loss-table">
        <thead>
          <tr>
            {tableHeaders.map((header) => (
              <th key={header}>{header}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              {tableHeaders.map((header) => (
                <td key={header}>{item[header.toLowerCase().replace(' ', '_')]}</td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ProfitLossTable;
