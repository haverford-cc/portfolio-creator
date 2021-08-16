import "../styles/globals.css";
import type { AppProps } from "next/app";
import * as axios from 'axios';
import { ApiContext } from '../helpers/ApiContext';

const MyApp = ({ Component, pageProps }: AppProps) => {
  
  const { ApiClient } = (axios as any).create({
    baseURL: "/api",
    withCredentials: true,
    // headers: { "X-Forwarded-Host":  },
  });

  return (
    <ApiContext.Provider value={ ApiClient }>
      <Component {...pageProps} />
    </ApiContext.Provider> 
  )
};

export default MyApp;
