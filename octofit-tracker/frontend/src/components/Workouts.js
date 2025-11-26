import React, { useEffect, useState } from "react";

const endpoint = (name) => {
  const host = process.env.REACT_APP_CODESPACE_NAME;
  const base = host ? `https://${host}-8000.app.github.dev` : "";
  return `${base}/api/${name}/`;
};

export default function Workouts() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const url = endpoint("workouts");
    console.log("Fetching Workouts from", url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log("Workouts response", json);
        const items = Array.isArray(json) ? json : json.results ?? [];
        setData(items);
      })
      .catch((err) => console.error("Workouts fetch error", err));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
