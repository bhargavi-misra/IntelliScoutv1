"use client";

import { extractWebsite } from "@/lib/api";

type MissionCardProps = {
  url: string;
  setUrl: (value: string) => void;

  prompt: string;
  setPrompt: (value: string) => void;

  loading: boolean;
  setLoading: (value: boolean) => void;

  onResults: (results: any[]) => void;
};

export default function MissionCard({
  url,
  setUrl,
  prompt,
  setPrompt,
  loading,
  setLoading,
  onResults,
}: MissionCardProps) {
  async function handleExtract() {
    if (!url.trim() || !prompt.trim()) {
      alert("Please fill in both fields.");
      return;
    }

    try {
      setLoading(true);

      const data = await extractWebsite(url, prompt);

      onResults(data.items);

    } catch (error) {
      console.error(error);
      alert("Extraction failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div
      className="
        w-full
        max-w-3xl
        rounded-3xl
        border
        border-white/10
        bg-white/5
        backdrop-blur-xl
        shadow-2xl
        p-8
        md:p-10
      "
    >
      <h2 className="pixel-font text-3xl mb-3">
        ✦ Extract Data From Any Website
      </h2>

      <p className="text-slate-400 mb-8">
        Describe the information you want and IntelliScout will extract it for
        you.
      </p>

      {/* URL */}

      <div className="mb-7">

        <label className="block mb-2 pixel-font text-sm">
          Website URL
        </label>

        <input
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="https://example.com"
          className="
            w-full
            rounded-xl
            bg-slate-900/70
            border
            border-slate-700
            px-5
            py-4
            outline-none
            transition
            focus:border-violet-400
          "
        />

      </div>

      {/* Prompt */}

      <div>

        <label className="block mb-2 pixel-font text-sm">
          What would you like to extract?
        </label>

        <textarea
          rows={5}
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Extract product title, price and rating..."
          className="
            w-full
            rounded-xl
            bg-slate-900/70
            border
            border-slate-700
            px-5
            py-4
            outline-none
            resize-none
            transition
            focus:border-violet-400
          "
        />

      </div>

      {/* Examples */}

      <div className="mt-5">

        <p className="pixel-font text-sm text-violet-300 mb-2">
          Examples
        </p>

        <ul className="space-y-2 text-sm text-slate-400">
          <li>• Product name, price and availability</li>
          <li>• Internship title, company, location and stipend</li>
          <li>• News headline, author and published date</li>
          <li>• Restaurant name, cuisine, rating and address</li>
        </ul>

      </div>

      {/* Button */}

      <button
        onClick={handleExtract}
        disabled={loading}
        className="
          mt-8
          w-full
          rounded-xl
          bg-violet-600
          py-4
          pixel-font
          transition-all
          hover:scale-[1.02]
          hover:bg-violet-500
          disabled:opacity-60
          disabled:cursor-not-allowed
        "
      >
        {loading ? "🔍 Scouting..." : "✨ Extract Data"}
      </button>

    </div>
  );
}