import type { AppProps } from "next/app";

import { ApiClientProvider } from "../hooks/api";
import "../styles/globals.css";

const MyApp = ({ Component, pageProps }: AppProps) => {
  return (
    <ApiClientProvider>
      <Component {...pageProps} />
    </ApiClientProvider>
  );
};

export default MyApp;
