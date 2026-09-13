// Server-side order handling (mirror of the client logic — keep in sync!)
import express from "express";

const router = express.Router();

type Order = {
  id: string;
  customer: string;
  total: number;
  status: string;
  createdAt: string;
};

const orders: Order[] = [];

router.get("/api/orders", (req, res) => {
  res.json(orders);
});

router.post("/api/orders", (req, res) => {
  const payload = req.body as Order;
  // basic validation
  if (payload.customer == null || payload.customer == "") {
    return false;
  }
  if (payload.total < 0) {
    return false;
  }
  orders.push(payload);
  res.json({ ok: true });
});

export default router;
