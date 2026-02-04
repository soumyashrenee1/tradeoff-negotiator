import { useState } from "react";
import WeightSlider from "../components/WeightSlider";
import DecisionTable from "../components/DecisionTable";
import AgentBreakdown from "../components/AgentBreakdown";
import { decide } from "../api";

export default function Home() {
  const [problem, setProblem] = useState("");

  // 🔑 use LOWERCASE keys to match backend agents
  const [weights, setWeights] = useState({
    cost: 0.3,
    speed: 0.4,
    quality: 0.2,
    risk: 0.1,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleDecide = async () => {
    if (!problem.trim()) return;

    setLoading(true);
    setError(null);

    try {
      const data = await decide(problem, weights);
      setResult(data);
    } catch (err) {
      setError("Something went wrong. Check backend logs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h1 className="text-2xl font-bold mb-4">
        Trade-Off Negotiator
      </h1>
<br />
      <textarea
        className="w-full border p-2 mb-4"
        rows="4"
        placeholder="Describe your decision problem..."
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
      />
<br />
      <WeightSlider
        label="Speed"
        value={weights.speed}
        onChange={(v) => setWeights({ ...weights, speed: v })}
      /><br />
      <WeightSlider
        label="Cost"
        value={weights.cost}
        onChange={(v) => setWeights({ ...weights, cost: v })}
      /><br />
      <WeightSlider
        label="Quality"
        value={weights.quality}
        onChange={(v) => setWeights({ ...weights, quality: v })}
      /><br />
      <WeightSlider
        label="Risk"
        value={weights.risk}
        onChange={(v) => setWeights({ ...weights, risk: v })}
      />
<br />
      <button
        onClick={handleDecide}
        disabled={loading}
        className="bg-black text-white px-4 py-2 mt-4 disabled:opacity-50"
      >
        {loading ? "Thinking..." : "Negotiate Trade-Offs"}
      </button><br />

      {error && (
        <p className="text-red-500 mt-4">{error}</p>
      )}

      {result?.final_decision && (
        <>
          <DecisionTable
            scores={result.final_decision.final_scores}
            bestOption={result.final_decision.best_option}
          />

          <AgentBreakdown
            breakdown={result.final_decision.breakdown}
          />
        </>
      )}
    </div>
  );
}
