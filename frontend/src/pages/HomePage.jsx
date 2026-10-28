import { useEffect, useState } from "react";
import api from "../services/api.js";

export default function HomePage() {
  const [backend, setBackend] = useState("checking...");

  useEffect(() => {
    api
      .get("/health/")
      .then(() => setBackend("connected"))
      .catch(() => setBackend("not reachable"));
  }, []);

  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <h1 className="text-2xl font-bold text-gray-900">Lab Project</h1>
      <p className="mt-1 text-sm text-gray-500">Backend: {backend}</p>
      <section className="mt-6 rounded-xl border border-gray-200 bg-white p-6">
        {/* Lab page goes here: insert form and records list. */}
      </section>
    </main>
  );
}
