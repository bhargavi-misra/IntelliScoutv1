"use client";

type Props = {
  message: string;
};

export default function ScoutBubble({ message }: Props) {
  return (
    <div
      className="
        absolute
        -top-12
        left-1/2
        -translate-x-1/2

        whitespace-nowrap

        rounded-xl

        border
        border-violet-400/20

        bg-slate-900/90

        px-4
        py-2

        backdrop-blur-xl

        shadow-lg
      "
    >
      <p className="pixel-font text-[10px] text-violet-200">
        {message}
      </p>

      {/* Bubble Arrow */}

      <div
        className="
          absolute

          left-1/2

          top-full

          -translate-x-1/2

          w-0
          h-0

          border-l-[7px]
          border-r-[7px]
          border-t-[8px]

          border-l-transparent
          border-r-transparent
          border-t-slate-900
        "
      />
    </div>
  );
}