import { useEffect, useState } from "react";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(`${API_URL}/`)
      .then(async (res) => {
        if (!res.ok) throw new Error("Erreur backend");
        return res.json();
      })
      .then(setData)
      .catch((err) => setError(err.message));
  }, []);

  return (
    <main className="page">
      <section className="card">
        <h1>Wine Starter Render Ready</h1>
        <p>Frontend React connecté à un backend FastAPI.</p>

        <div className="meta">
          <span>API :</span>
          <code>{API_URL}</code>
        </div>

        {error && <p className="error">{error}</p>}

        {data && (
          <div className="result">
            <p><strong>Message :</strong> {data.message}</p>
            <p><strong>Base :</strong> {data.database}</p>
            <p><strong>Heure :</strong> {new Date(data.time).toLocaleString("fr-FR")}</p>
          </div>
        )}
      </section>
    </main>
  );
}
