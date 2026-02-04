export default function WeightSlider({ label, value, onChange }) {
  return (
    <div className="mb-4">
      <label className="block font-medium mb-1">
        {label}: {(value * 100).toFixed(0)}%
      </label>
      <input
        type="range"
        min="0"
        max="1"
        step="0.05"
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        className="w-full"
      />
    </div>
  );
}
