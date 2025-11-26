import React, { useEffect, useState } from "react";

const endpoint = (name) => {
  const host = process.env.REACT_APP_CODESPACE_NAME;
  const base = host ? `https://${host}-8000.app.github.dev` : "";
  return `${base}/api/${name}/`;
};

export default function Leaderboard() {
  const [data, setData] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    const url = endpoint("leaderboard");
    const exampleUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    console.log("Fetching Leaderboard from", url);
    console.log("Example Leaderboard endpoint (literal):", exampleUrl);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log("Leaderboard response", json);
        const items = Array.isArray(json) ? json : json.results ?? [];
        setData(items);
      })
      .catch((err) => console.error("Leaderboard fetch error", err));
  }, []);

  return (
    <div className="container app-container">
      <div className="card card-table">
        <div className="card-body">
          <h3 className="card-title">Leaderboard</h3>
          <p className="small-muted">Top performers from REST API</p>

          <table className="table table-striped table-fixed">
            <thead>
              <tr>
                <th style={{ width: "10%" }}>Rank</th>
                <th style={{ width: "50%" }}>User</th>
                <th style={{ width: "20%" }}>Score</th>
                <th style={{ width: "20%" }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {data.map((it, idx) => (
                <tr key={it.id ?? idx}>
                  <td>{it.rank ?? idx + 1}</td>
                  <td>{it.user?.username ?? it.user ?? it.name ?? "—"}</td>
                  <td>{it.score ?? it.points ?? "—"}</td>
                  <td>
                    <button
                      className="btn btn-sm btn-primary me-2"
                      onClick={() => setSelected(it)}
                    >
                      View
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {selected && (
            <div className="modal show d-block" tabIndex="-1">
              <div className="modal-dialog">
                <div className="modal-content">
                  <div className="modal-header">
                    <h5 className="modal-title">Leaderboard Item</h5>
                    <button
                      type="button"
                      className="btn-close"
                      aria-label="Close"
                      onClick={() => setSelected(null)}
                    />
                  </div>
                  <div className="modal-body">
                    <pre>{JSON.stringify(selected, null, 2)}</pre>
                  </div>
                  <div className="modal-footer">
                    <button
                      className="btn btn-secondary"
                      onClick={() => setSelected(null)}
                    >
                      Close
                    </button>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
