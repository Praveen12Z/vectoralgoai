export default function Product() {
  return (
    <main className="px-8 py-20 max-w-6xl mx-auto">
      <h2 className="text-4xl font-bold mb-6">
        Strategy Crash-Test Lab
      </h2>

      <p className="text-lg text-slate-600 dark:text-slate-300 max-w-3xl">
        Design strategies, inspect every trade, and receive AI-driven critique —
        without blind prediction models.
      </p>

      <div className="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6">
        {["Strategy Builder", "Trade Inspector", "AI Commentary"].map((item) => (
          <div key={item} className="border rounded-xl p-6">
            <h3 className="font-semibold">{item}</h3>
            <p className="text-sm text-slate-500 mt-2">
              Preview module
            </p>
          </div>
        ))}
      </div>
    </main>
  );
}
