import "../styles/globals.css";
import type { AppProps } from "next/app";
import { createContext } from "react";
import * as axios from 'axios';

const MyApp = ({ Component, pageProps }: AppProps) => {
  const ApiClient = axios.create({
    baseURL: "/api",
    withCredentials: true,
    // headers: { "X-Forwarded-Host":  },
  });

  const ApiContext = createContext(ApiClient);

  return (
    <ApiContext.Provider value={ ApiContext }>
      <Component {...pageProps} />
    </ApiContext.Provider> 
  )
};

export default MyApp;
