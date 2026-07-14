"use client";

import { useState } from "react";

import MoonGlow from "@/components/background/MoonGlow";
import StarField from "@/components/background/StarField";

import Scout from "@/components/mascot/Scout";

import MissionCard from "@/components/form/MissionCard";
import ResultsPanel from "@/components/results/ResultsPanel";

import Footer from "@/components/ui/Footer";

export default function Home() {
  const [url, setUrl] = useState("");
  const [prompt, setPrompt] = useState("");

  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  return (
    <main className="relative min-h-screen overflow-hidden">

      {/* Background */}
      <MoonGlow />
      <StarField />
      <Scout />

      {/* Content */}
      <section className="relative z-10 flex flex-col items-center px-6 pt-20 pb-20">

        {/* Hero */}

        <div className="text-center">

          <div className="mb-6 flex items-center justify-center gap-8">

            <span className="pixel-star">✦</span>

            <h1 className="pixel-font glow-title text-7xl md:text-8xl">
              IntelliScout
            </h1>

            <span className="pixel-star">✦</span>

          </div>

          <p className="pixel-font subtitle text-lg">
            Your AI Web Research Assistant
          </p>

          <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-400">
            Extract structured data from any website using natural language.
            No CSS selectors. No coding. Just describe what you need.
          </p>

        </div>

        {/* Mission Card */}

        <div className="mt-20 flex w-full justify-center">

          <MissionCard
            url={url}
            setUrl={setUrl}
            prompt={prompt}
            setPrompt={setPrompt}
            loading={loading}
            setLoading={setLoading}
            onResults={setResults}
          />

        </div>

        {/* Results */}

        <ResultsPanel
    results={results}
/>

      </section>

      <Footer />

    </main>
  );
}