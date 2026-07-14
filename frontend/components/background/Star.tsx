"use client";

import { motion } from "framer-motion";

type StarProps = {
  top: number;
  left: number;
  size: number;
  duration: number;
  delay: number;
  color: string;
};

export default function Star({
  top,
  left,
  size,
  duration,
  delay,
  color,
}: StarProps) {
  return (
    <motion.div
      className="absolute"
      style={{
        top: `${top}%`,
        left: `${left}%`,
      }}
      animate={{
        opacity: [0.2, 1, 0.2],
        scale: [1, 1.3, 1],
      }}
      transition={{
        duration,
        repeat: Infinity,
        delay,
        ease: "easeInOut",
      }}
    >
      <div
        style={{
          display: "grid",
          gridTemplateColumns: `repeat(3, ${size}px)`,
          gridTemplateRows: `repeat(3, ${size}px)`,
        }}
      >
        {[0,1,2,3,4,5,6,7,8].map((i) => (
          <div
            key={i}
            style={{
              width: size,
              height: size,
              background:
                [1,3,4,5,7].includes(i)
                  ? color
                  : "transparent",
            }}
          />
        ))}
      </div>
    </motion.div>
  );
}