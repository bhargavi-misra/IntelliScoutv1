export default function MoonGlow() {
  return (
    <div
      className="fixed -top-64 -left-64 w-[900px] h-[900px] rounded-full pointer-events-none z-0"
      style={{
        background:
          "radial-gradient(circle, rgba(150,180,255,.35) 0%, rgba(120,130,255,.18) 35%, transparent 70%)",
        filter: "blur(120px)",
      }}
    />
  );
}