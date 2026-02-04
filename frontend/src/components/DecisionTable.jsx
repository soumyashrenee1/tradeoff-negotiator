export default function DecisionTable({ scores, bestOption }) {
  if (!scores) return null;

  return (
    <div className="mt-6">
      <h2 className="text-xl font-semibold mb-2">Final Ranking</h2>

      <table className="w-full border">
        <thead>
          <tr className="bg-gray-100">
            <th className="border p-9 text-left">Option</th>
            <th className="border p-9">Score</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(scores)
            .sort((a, b) => b[1] - a[1])
            .map(([option, score]) => (
              <tr
                key={option}
                className={
                  option === bestOption
                    ? "bg-green-100 font-semibold"
                    : ""
                }
              >
                <td className="border p-9 text-center">{option}</td>
                <td className="border p-9 text-center">{score}</td>
              </tr>
            ))}
        </tbody>
      </table>

      <p className="mt-3">
        ✅ <strong>Best Option:</strong> {bestOption}
      </p>
    </div>
  );
}
