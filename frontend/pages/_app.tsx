import type { AppProps } from "next/app";
import Navbar from "../components/Navbar/Narbar";

import { ApiClientProvider } from "../hooks/api";
import "../styles/globals.css";

const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
    <ApiClientProvider>
      <Navbar />
      <Component {...pageProps} />
    </ApiClientProvider>
  );
};

export default MyApp;
