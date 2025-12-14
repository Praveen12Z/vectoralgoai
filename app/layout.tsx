import "./globals.css";
import Navbar from "@/components/Navbar";

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-slate-900 dark:bg-slate-950 dark:text-slate-100">
        <Navbar />
        {children}
      </body>
    </html>
  );
}

