import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState({
    sump_level: 0,
    oht_level: 0,
    motor_status: 0,
  });

  const loadData = () => {
    fetch("http://127.0.0.1:5000/api/latest-data")
      .then((response) => response.json())
      .then((result) => {
        setData(result);
      });
  };

  useEffect(() => {
    loadData();

    const interval = setInterval(() => {
      loadData();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <h1>Arjun Flat Water Automation</h1>

      <div className="card-container">

        <div className="card">
          <h2>SUMP LEVEL</h2>
          <h1>{data.sump_level}%</h1>

          <div className="progress">
            <div
              className="fill"
              style={{ width: `${data.sump_level}%` }}
            ></div>
          </div>
        </div>

        <div className="card">
          <h2>OHT LEVEL</h2>
          <h1>{data.oht_level}%</h1>

          <div className="progress">
            <div
              className="fill"
              style={{ width: `${data.oht_level}%` }}
            ></div>
          </div>
        </div>

        <div
          className={
            data.motor_status === 1
              ? "card motor-on"
              : "card motor-off"
          }
        >
          <h2>MOTOR STATUS</h2>

          <h1>
            {data.motor_status === 1 ? "ON" : "OFF"}
          </h1>
        </div>

      </div>
    </div>
  );
}

export default App;