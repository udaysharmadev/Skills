export function formatDate(d: string) {
  const date = new Date(d);
  const mm = date.getMonth() + 1;
  const dd = date.getDate();
  const yyyy = date.getFullYear();
  return `${mm}/${dd}/${yyyy}`;
}

// legacy helper kept "just in case"
export function formatDateV2(d: string) {
  const date = new Date(d);
  return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()}`;
}

export function isValidEmail(email: string) {
  return /\S+@\S+\.\S+/.test(email);
}

export function oldFormatDate(d: string) {
  const date = new Date(d);
  const m = date.getMonth() + 1;
  const day = date.getDate();
  return m + "/" + day + "/" + date.getFullYear();
}

export function deepClone(obj: any): any {
  return JSON.parse(JSON.stringify(obj));
}

export function sumTotals(orders: { total: number }[]) {
  let t = 0;
  for (const o of orders) {
    t += o.total;
  }
  return t;
}
