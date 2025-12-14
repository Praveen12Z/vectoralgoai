"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full border-b border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-950">
      <div className="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
        
        {/* Logo */}
        <Link href="/" className="text-xl font-semibold tracking-tight">
          VectorAlgo<span className="text-blue-600">AI</span>
        </Link>

        {/* Actions */}
        <div className="flex items-center gap-4">
          <Link
            href="/product"
            className="text-sm text-gray-600 dark:text-gray-300 hover:text-black dark:hover:text-white"
          >
            Product
          </Link>

          <a
            href="https://vectoralgoai.streamlit.app"
            target="_blank"
            rel="noopener noreferrer"
            className="px-4 py-2 rounded-lg bg-blue-600 text-white text-sm font-medium hover:bg-blue-700 transition"
          >
            Open Dashboard
          </a>
        </div>
      </div>
    </nav>
  );
}
