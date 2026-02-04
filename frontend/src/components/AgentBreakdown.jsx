export default function AgentBreakdown({ breakdown }) {
  if (!breakdown) return null;

  return (
    <div className="mt-8">
      <h2 className="text-xl font-semibold mb-3">
        Agent Reasoning Breakdown
      </h2>

      {Object.entries(breakdown).map(([option, agents]) => (
        <div key={option} className="mb-6 border p-4 rounded">
          <h3 className="font-bold text-lg mb-2">{option}</h3>

          {Object.entries(agents).map(([agent, data]) => (
            <div key={agent} className="mb-3">
              <p className="font-semibold capitalize">
                {agent} Agent
              </p>
              <p className="text-sm">
                Raw Score: <strong>{data.raw_score}</strong> | Weighted:{" "}
                <strong>{data.weighted_score}</strong>
              </p>
              <p className="text-sm text-gray-700">
                {data.reasoning}
              </p>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
}
