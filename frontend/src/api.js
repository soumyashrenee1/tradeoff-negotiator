export async function decide(question, weights) {
  const res = await fetch("http://127.0.0.1:8000/decide", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      question,
      weights,
    }),
  });

  if (!res.ok) {
    throw new Error("Decision failed");
  }

  return res.json();
}
