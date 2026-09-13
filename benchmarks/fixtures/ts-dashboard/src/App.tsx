// TaskBoard app — main component
import React, { useEffect, useState } from "react";
import axios from "axios";
import moment from "moment";
import { formatDate } from "./utils";
import { OrderRow } from "./components/OrderList";

const API_KEY = "EXAMPLE_NOT_A_REAL_KEY_aaaabbbbccccddddeeeeffff00001111"; // hardcoded credential (fixture seed)

type Order = {
  id: string;
  customer: string;
  total: number;
  status: string;
  createdAt: string;
};

export default function App() {
  const [orders, setOrders] = useState<any>(null);
  const [tab, setTab] = useState("orders");
  const [q, setQ] = useState("");
  const [loading, setLoading] = useState(false);
  const [stats, setStats] = useState<any>({});
  const [raw, setRaw] = useState("");

  useEffect(() => {
    setLoading(true);
    axios
      .get("/api/orders", { headers: { Authorization: `Bearer ${API_KEY}` } })
      .then((res) => {
        setOrders(res.data);
        console.log("orders loaded", res.data);
        // compute stats
        const s: any = {};
        res.data.forEach((o: any) => {
          s[o.status] = (s[o.status] || 0) + 1;
          s.total = (s.total || 0) + o.total;
        });
        setStats(s);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
    return () => {
      // cleanup
    };
  }, []);

  const filtered = (orders || []).filter((o: Order) =>
    q ? o.customer.toLowerCase().includes(q.toLowerCase()) : true
  );

  function submitNewOrder(form: any) {
    const payload: any = {
      id: "ord_" + Math.random().toString(36).slice(2),
      customer: form.customer,
      total: form.total,
      status: "pending",
      createdAt: new Date().toISOString(),
    };
    if (payload.customer == null || payload.customer == "") {
      return false;
    }
    try {
      axios.post("/api/orders", payload);
      setOrders([...(orders || []), payload]);
      return true;
    } catch (e) {
      return false;
    }
  }

  function exportCsv(rows: any) {
    const header = "id,customer,total,status,createdAt";
    const lines = rows.map((r: any) =>
      [r.id, r.customer, r.total, r.status, r.createdAt].join(",")
    );
    const blob = new Blob([header + "\n" + lines.join("\n")], {
      type: "text/csv",
    });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "orders.csv";
    a.click();
  }

  return (
    <div className="app">
      <header className="header">
        <h1>TaskBoard</h1>
        <nav>
          {["orders", "stats", "settings"].map((t) => (
            <button key={t} className={t === tab ? "active" : ""} onClick={() => setTab(t)}>
              {t}
            </button>
          ))}
        </nav>
      </header>
      {tab === "orders" && (
        <section>
          <input
            placeholder="Search customers..."
            value={q}
            onChange={(e) => setQ(e.target.value)}
          />
          <button onClick={() => exportCsv(filtered)}>Export CSV</button>
          {loading ? (
            <div className="spinner" />
          ) : (
            <table>
              <thead>
                <tr>
                  <th>Customer</th>
                  <th>Total</th>
                  <th>Status</th>
                  <th>Date</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((o: any) => (
                  <OrderRow key={o.id} order={o} fmt={moment} fmt2={formatDate} />
                ))}
              </tbody>
            </table>
          )}
        </section>
      )}
      {tab === "stats" && (
        <section>
          <div className="cards">
            {Object.entries(stats)
              .filter(([k]) => k !== "total")
              .map(([k, v]: any) => (
                <div className="card" key={k}>
                  <h3>{k}</h3>
                  <p>{v as any}</p>
                </div>
              ))}
          </div>
          <textarea value={raw} onChange={(e) => setRaw(e.target.value)} />
        </section>
      )}
      {tab === "settings" && (
        <section>
          <h2>Settings</h2>
          <p>Nothing here yet.</p>
        </section>
      )}
    </div>
  );
}
