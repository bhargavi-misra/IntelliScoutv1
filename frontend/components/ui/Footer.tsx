"use client";

import { useMemo } from "react";
import { useEffect, useState } from "react";

const messages = [
  "🐾 Thanks for visiting!",
  "🌙 Ready for another adventure?",
  "✨ Tell me what to extract!",
  "📦 Let's gather some data!",
  "🛰️ The web is waiting to be explored.",
  "💜 Hope you enjoy IntelliScout!",
  "🔍 What shall we scout today?",
  "⭐ Have an awesome day!",
  "📚 Every website hides a story.",
  "🚀 Ready to scout the web!",
];

export default function Footer() {

  const [message, setMessage] = useState(messages[0]);

useEffect(() => {
  let index = 0;

  const interval = setInterval(() => {
    index = (index + 1) % messages.length;
    setMessage(messages[index]);
  }, 4000);

  return () => clearInterval(interval);
}, []);

  return (
    <footer className="relative z-10 mt-20 pb-8 flex justify-center">

      <div className="group relative">

        {/* Card */}

        <div
          className="
            rounded-xl
            border
            border-violet-400/20

            bg-slate-950/40
            backdrop-blur-xl

            px-6
            py-4

            shadow-[0_0_24px_rgba(124,108,255,0.15)]

            transition-all
            duration-300

            hover:border-violet-400/40
            hover:shadow-[0_0_36px_rgba(124,108,255,0.28)]

            cursor-default
          "
        >

          <p className="pixel-font text-[11px] tracking-[0.28em] text-center text-violet-300">

            🐈 SCOUT'S CREATOR

          </p>

          <p className="pixel-font mt-2 text-center text-base text-slate-200">

            Bhargavi Misra

          </p>

        </div>

        {/* Tooltip */}

        <div
          className="
            absolute

            bottom-full

            left-1/2

            -translate-x-1/2

            mb-4

            opacity-0

            translate-y-2

            group-hover:translate-y-0
            group-hover:opacity-100

            transition-all
            duration-300

            pointer-events-none
          "
        >

          <div
            className="
              rounded-xl

              border
              border-violet-400/20

              bg-slate-950/95

              backdrop-blur-xl

              px-5
              py-4

              shadow-2xl

              whitespace-nowrap
            "
          >

            <p className="pixel-font text-[10px] tracking-widest text-violet-300">

              SCOUT SAYS...

            </p>

            <p className="mt-2 text-sm text-slate-300">

              {message}

            </p>

          </div>

        </div>

      </div>

    </footer>
  );
}