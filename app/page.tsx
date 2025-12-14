export default function Home() {
  return (
    <main className="px-8 py-20 max-w-6xl mx-auto">
      <h1 className="text-5xl font-bold mb-6">
        VectorAlgoAI
      </h1>

      <p className="text-xl text-slate-600 dark:text-slate-300 max-w-2xl">
        AI-powered strategy engineering for serious traders.
        Build, stress-test, and understand trading systems — with explainability.
      </p>

      <div className="mt-10 flex gap-4">
        <a href="/product" className="px-6 py-3 bg-blue-600 text-white rounded-lg">
          View Product
        </a>
        <a href="#" className="px-6 py-3 border rounded-lg">
          Open Dashboard
        </a>
      </div>
    </main>
  );
}

