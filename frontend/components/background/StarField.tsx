"use client";

import { useEffect, useState } from "react";
import Star from "./Star";

type StarType = {
  id: number;
  top: number;
  left: number;
  size: number;
  duration: number;
  delay: number;
  color: string;
};

const colors = [
  "#F7F3E8",
  "#F7F3E8",
  "#F7F3E8",
  "#F7F3E8",
  "#F7F3E8",
  "#B79DFF",
  "#8EC8FF",
];

export default function StarField() {
  const [stars, setStars] = useState<StarType[]>([]);

  useEffect(() => {
    const generated = Array.from({ length: 55 }, (_, i) => {
      let top = Math.random() * 100;
      let left = Math.random() * 100;

      // Keep the hero area clean
      while (
        top > 28 &&
        top < 72 &&
        left > 18 &&
        left < 82
      ) {
        top = Math.random() * 100;
        left = Math.random() * 100;
      }

      return {
        id: i,
        top,
        left,
        size:
          Math.random() < 0.7
            ? 1
            : Math.random() < 0.95
            ? 2
            : 3,
        duration: Math.random() * 3 + 3,
        delay: Math.random() * 5,
        color: colors[Math.floor(Math.random() * colors.length)],
      };
    });

    setStars(generated);
  }, []);

  return (
  <div className="fixed inset-0 z-10 overflow-hidden pointer-events-none">
    {stars.map((star) => (
      <Star key={star.id} {...star} />
    ))}
  </div>
);
}