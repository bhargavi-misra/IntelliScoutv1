"use client";

import Image from "next/image";
import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import ScoutBubble from "./ScoutBubble";

const positions = [
  { x: -560, y: -280 },
  { x: 520, y: -250 },

  { x: -610, y: -40 },
  { x: 570, y: 10 },

  { x: -520, y: 260 },
  { x: 520, y: 280 },
];

const messages = [
  "Ready to scout! 🔍",
  "Need a website 🌐",
  "Let's explore! ✨",
  "What shall I extract? 📦",
  "I'm watching the web 👀",
];

export default function Scout() {
  const [target, setTarget] = useState(0);
  const [message, setMessage] = useState(messages[0]);

  // Wander around the edges
  useEffect(() => {
    const interval = setInterval(() => {
      setTarget((prev) => {
        let next = prev;

        while (next === prev) {
          next = Math.floor(Math.random() * positions.length);
        }

        return next;
      });
    }, 9000);

    return () => clearInterval(interval);
  }, []);

  // Rotate speech bubbles
  useEffect(() => {
    const interval = setInterval(() => {
      setMessage(
        messages[Math.floor(Math.random() * messages.length)]
      );
    }, 7000);

    return () => clearInterval(interval);
  }, []);

  return (
    <motion.div
      className="fixed left-1/2 top-1/2 z-10 pointer-events-none"
      animate={{
        x: positions[target].x,
        y: positions[target].y,
      }}
      transition={{
        x: {
          duration: 6,
          ease: "easeInOut",
        },
        y: {
          duration: 6,
          ease: "easeInOut",
        },
      }}
    >
      <motion.div
        animate={{
          y: [0, -8, 0],
          rotate: [-2, 2, -2],
          scale: [1, 1.03, 1],
        }}
        transition={{
          y: {
            duration: 2.8,
            repeat: Infinity,
            ease: "easeInOut",
          },
          rotate: {
            duration: 4,
            repeat: Infinity,
            ease: "easeInOut",
          },
          scale: {
            duration: 2.8,
            repeat: Infinity,
            ease: "easeInOut",
          },
        }}
      >
        <ScoutBubble message={message} />

        <Image
          src="/mascot/scout_idle.png"
          alt="Scout"
          width={170}
          height={170}
          priority
          draggable={false}
        />
      </motion.div>
    </motion.div>
  );
}