"use client";

import { downloadCSV } from "@/lib/api";

type Props = {
  results: Record<string, any>[];
};

export default function ResultsPanel({
  results,
}: Props) {

  if (!results.length) {
    return (
      <section className="mt-16 w-full max-w-6xl">

        <div
          className="
          rounded-3xl
          border
          border-white/10
          bg-white/5
          backdrop-blur-xl
          p-12
          text-center
          "
        >

          <div className="text-6xl mb-6">
            🐱
          </div>

          <h2 className="pixel-font text-3xl mb-4">
            Scout is Waiting...
          </h2>

          <p className="text-slate-400">
            Enter a website URL and describe what you'd like to extract.
          </p>

        </div>

      </section>
    );
  }

  function copyJSON() {
    navigator.clipboard.writeText(
      JSON.stringify(results, null, 2)
    );
  }

  async function handleDownload() {
    try {

      await downloadCSV(results);

    } catch (err) {

      console.error(err);

      alert("Couldn't generate CSV.");

    }
  }

  return (
    <section className="mt-16 w-full max-w-6xl">

      {/* Header */}

      <div
        className="
        rounded-3xl
        border
        border-white/10
        bg-white/5
        backdrop-blur-xl
        p-8
        mb-8
        "
      >

        <div className="flex flex-wrap justify-between items-center gap-4">

          <div>

            <h2 className="pixel-font text-3xl">
              ✦ Extraction Complete
            </h2>

            <p className="mt-3 text-slate-400">
              Scout found{" "}
              <span className="text-violet-300 font-semibold">
                {results.length}
              </span>{" "}
              structured items.
            </p>

          </div>

          <div className="flex gap-3">

            <button
              onClick={copyJSON}
              className="
              rounded-xl
              border
              border-violet-500/30
              px-5
              py-3
              hover:bg-violet-500/20
              transition
              "
            >
              📋 Copy JSON
            </button>

            <button
              onClick={handleDownload}
              className="
              rounded-xl
              bg-violet-600
              px-5
              py-3
              hover:bg-violet-500
              transition
              "
            >
              📥 Download CSV
            </button>

          </div>

        </div>

      </div>

      {/* Cards */}

      <div className="grid gap-6">

        {results.map((item, index) => (

          <div
            key={index}
            className="
            rounded-3xl
            border
            border-white/10
            bg-white/5
            backdrop-blur-xl
            p-6
            shadow-xl
            "
          >

            <div className="flex items-center justify-between mb-6">

              <h3 className="pixel-font text-2xl">
                📦 Item #{index + 1}
              </h3>

            </div>

            <div className="space-y-4">

              {Object.entries(item).map(([key, value]) => (

                <div
                  key={key}
                  className="
                  rounded-xl
                  bg-slate-900/40
                  p-4
                  "
                >

                  <p className="pixel-font text-xs text-violet-300 uppercase tracking-wider">

                    {key.replaceAll("_", " ")}

                  </p>

                  <p className="mt-2 text-slate-200 break-words">

                    {String(value)}

                  </p>

                </div>

              ))}

            </div>

          </div>

        ))}

      </div>

    </section>
  );
}