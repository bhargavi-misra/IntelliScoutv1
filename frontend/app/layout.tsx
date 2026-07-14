import type { Metadata } from "next";
import { Inter, Pixelify_Sans } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

const pixelify = Pixelify_Sans({
  subsets: ["latin"],
  variable: "--font-pixel",
});

export const metadata: Metadata = {
  title: "IntelliScout",
  description: "AI Web Research Assistant",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${inter.variable} ${pixelify.variable}`}>
        {children}
      </body>
    </html>
  );
}