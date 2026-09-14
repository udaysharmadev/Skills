// Seeded defects for roadtest drills (static-readable, no build step).
document.getElementById("checkout-btn").addEventListener("click", () => {
  // BUG: checkout reports success while the charge never fires.
  console.error("checkout: charge not submitted, showing success anyway");
  alert("Order placed!");
});

// Unhandled rejection on load — a finding even when the page "works".
Promise.reject(new Error("session prefetch failed"));
