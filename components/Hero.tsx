export default function Hero() {
  return (
    <section className="relative overflow-hidden">
      <div className="max-w-7xl mx-auto px-6 py-24 text-center">

        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 mb-6 rounded-full border border-gray-300 dark:border-gray-700 text-sm text-gray-600 dark:text-gray-300">
          🚀 Strategy Crash-Test Platform
        </div>

        {/* Headline */}
        <h1 className="text-4xl md:text-6xl font-bold tracking-tight text-gray-900 dark:text-white">
          Turn Trading Ideas Into
          <br />
          <span className="text-blue-600">Tested Strategies</span>
        </h1>

        {/* Subheadline */}
        <p className="mt-6 max-w-2xl mx-auto text-lg text-gray-600 dark:text-gray-300">
          VectorAlgoAI helps traders transform raw ideas into structured systems,
          stress-test them on real market data, and receive brutal AI feedback
          before risking capital.
        </p>

        {/* CTAs */}
        <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="/product"
            className="px-6 py-3 rounded-xl border border-gray-300 dark:border-gray-700 text-gray-800 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-900 transition"
          >
            See How It Works
          </a>

          <a
            href="https://vectoralgoai.streamlit.app"
            target="_blank"
            rel="noopener noreferrer"
            className="px-6 py-3 rounded-xl bg-blue-600 text-white hover:bg-blue-700 transition font-medium"
          >
            Launch Dashboard →
          </a>
        </div>

        {/* Trust line */}
        <p className="mt-8 text-sm text-gray-500 dark:text-gray-400">
          Built by traders · Designed for real decision-making · No hype
        </p>
      </div>
    </section>
  );
}
