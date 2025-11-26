import React, { useEffect, useState } from 'react';

const endpoint = (name) => {
  const host = process.env.REACT_APP_CODESPACE_NAME;
  const base = host ? `https://${host}-8000.app.github.dev` : '';
  return `${base}/api/${name}/`;
};

export default function Workouts() {
  const [data, setData] = useState([]);
  const [selected, setSelected] = useState(null);

  useEffect(() => {
    const url = endpoint('workouts');
    console.log('Fetching Workouts from', url);
    fetch(url)
      .then((r) => r.json())
      .then((json) => {
        console.log('Workouts response', json);
        const items = Array.isArray(json) ? json : (json.results ?? []);
        setData(items);
      })
      .catch((err) => console.error('Workouts fetch error', err));
  }, []);

  return (
    <div className="container app-container">
      <div className="card card-table">
        <div className="card-body">
          <h3 className="card-title">Workouts</h3>
          <p className="small-muted">Workouts from REST API</p>

          <table className="table table-striped table-fixed">
            <thead>
              <tr>
                <th style={{width: '30%'}}>Title</th>
                <th style={{width: '50%'}}>Description</th>
                <th style={{width: '20%'}}>Actions</th>
              </tr>
            </thead>
            <tbody>
              {data.map((it, idx) => (
                <tr key={it.id ?? idx}>
                  <td>{it.title ?? it.name ?? '—'}</td>
                  <td>{it.description ?? it.summary ?? '—'}</td>
                  <td>
                    <button className="btn btn-sm btn-primary me-2" onClick={() => setSelected(it)}>View</button>
                    <button className="btn btn-sm btn-outline-secondary">Start</button>
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
                    <h5 className="modal-title">Workout Details</h5>
                    <button type="button" className="btn-close" aria-label="Close" onClick={() => setSelected(null)} />
                  </div>
                  <div className="modal-body">
                    <pre>{JSON.stringify(selected, null, 2)}</pre>
                  </div>
                  <div className="modal-footer">
                    <button className="btn btn-secondary" onClick={() => setSelected(null)}>Close</button>
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
