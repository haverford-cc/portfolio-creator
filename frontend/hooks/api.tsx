import {
  Dispatch,
  ReactNode,
  SetStateAction,
  createContext,
  useContext,
  useEffect,
  useState,
} from "react";

import axios, { AxiosInstance } from "axios";

type ApiClientType = {
  apiClient: AxiosInstance;
  host?: string;
  setHost: Dispatch<SetStateAction<string | undefined>>;
};

type ApiClientProviderProps = {
  host?: string;
  children: ReactNode;
};

const ApiClientContext = createContext<ApiClientType>(undefined!);

export const ApiClientProvider = (props: ApiClientProviderProps) => {
  const [host, setHost] = useState(props.host);

  const apiClient = axios.create({
    baseURL: "/api",
    withCredentials: true,
    headers: { "X-Forwarded-Host": host },
  });

  useEffect(() => {
    if (host) {
      apiClient.defaults.headers = { "X-Forwarded-Host": host };
    } else {
      apiClient.defaults.headers = {};
    }
  }, [apiClient, host]);

  return (
    <ApiClientContext.Provider value={{ apiClient, host, setHost }}>
      {props.children}
    </ApiClientContext.Provider>
  );
};

export const useApiClient = () => useContext(ApiClientContext);
