import React, { useEffect, useState } from "react";

const endpoint = (name) => {
  const host = process.env.REACT_APP_CODESPACE_NAME;
  const base = host ? `https://${host}-8000.app.github.dev` : "";
  return `${base}/api/${name}/`;
};

export default function Activities() {
  const [data, setData] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    const url = endpoint("activities");
    console.log("Fetching Activities from", url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log("Activities response", json);
        const items = Array.isArray(json) ? json : json.results ?? [];
        setData(items);
      })
      .catch((err) => console.error("Activities fetch error", err));
  }, []);

  return (
    <div className="container app-container">
      <div className="card card-table">
        <div className="card-body">
          <h3 className="card-title">Activities</h3>
          <p className="small-muted">Data from REST API</p>

          <table className="table table-striped table-fixed">
            <thead>
              <tr>
                <th style={{ width: "30%" }}>Name</th>
                <th style={{ width: "50%" }}>Description</th>
                <th style={{ width: "20%" }}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {data.map((it, idx) => (
                <tr key={it.id ?? idx}>
                  <td>{it.name ?? it.title ?? "—"}</td>
                  <td>{it.description ?? it.summary ?? "—"}</td>
                  <td>
                    <button
                      className="btn btn-sm btn-primary me-2"
                      onClick={() => setSelected(it)}
                    >
                      View
                    </button>
                    <a
                      className="btn btn-sm btn-outline-secondary"
                      href={`#`}
                      onClick={(e) => e.preventDefault()}
                    >
                      Edit
                    </a>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>

          {/* Modal (simple) */}
          {selected && (
            <div className="modal show d-block" tabIndex="-1" role="dialog">
              <div className="modal-dialog" role="document">
                <div className="modal-content">
                  <div className="modal-header">
                    <h5 className="modal-title">Activity Details</h5>
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
                      type="button"
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
