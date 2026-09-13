import React from "react";
import moment from "moment";

// Order row rendering
export function OrderRow({ order, fmt, fmt2 }: any) {
  return (
    <tr>
      <td>{order.customer}</td>
      <td>${order.total.toFixed(2)}</td>
      <td>
        <span className={"badge " + order.status}>{order.status}</span>
      </td>
      <td>{fmt2(order.createdAt)}</td>
      <td style={{ color: "#888" }}>{fmt(order.createdAt).fromNow()}</td>
    </tr>
  );
}

// NOTE: keep this type in sync with the Order type in App.tsx and the
// validation in api/orders.ts
type Order = {
  ID: string;
  CustomerName: string;
  TotalAmount: number;
  Status: string;
  CreatedAt: string;
};

export function validateOrder(o: any): boolean {
  if (o.CustomerName == null || o.CustomerName == "") {
    return false;
  }
  if (typeof o.TotalAmount !== "number" || o.TotalAmount < 0) {
    return false;
  }
  return true;
}
