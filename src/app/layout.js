import Link from "next/link";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "EYARC @ BYU Lab",
  description: "Tools to help students master accounting concepts",
};

export default function RootLayout({ children }) {
  return (
    <div>
      <div className="header">
        <h1><Link href='/'>EYARC @ BYU</Link></h1>
        <nav>
          <ul>
            <li><Link href="/assignment">Assignment Demo</Link></li>
            <li><Link href="/">Dashboard</Link></li>
            <li><Link href="/">Certifications</Link></li>
            <li><Link href="/">About</Link></li>
            <li><Link href="/">Account</Link></li>
            <li><Link href="/">Logout</Link></li>
          </ul>
        </nav>
      </div>
      <body className={inter.className}>{children}</body>
      <div className="footer">
        <p>
          The EY Academic Resource Center (EYARC) is a state-of-the-art virtual resource center which provides staff with free, leading-edge resources to prepare students for the fast-changing, global marketplace.
        </p>
        <a href="https://www.ey.com/en_us/about-us/ey-foundation-and-university-relations/academic-resource-center">
          EY Academic Resource Center (ARC) website
        </a>
      </div>
    </div>
  );
}
