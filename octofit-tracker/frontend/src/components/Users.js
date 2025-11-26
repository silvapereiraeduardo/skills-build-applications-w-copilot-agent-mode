import React, { useEffect, useState } from "react";

const endpoint = (name) => {
  const host = process.env.REACT_APP_CODESPACE_NAME;
  const base = host ? `https://${host}-8000.app.github.dev` : "";
  return `${base}/api/${name}/`;
};

export default function Users() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const url = endpoint("users");
    console.log("Fetching Users from", url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log("Users response", json);
        const items = Array.isArray(json) ? json : json.results ?? [];
        setData(items);
      })
      .catch((err) => console.error("Users fetch error", err));
  }, []);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
