import { store } from "@/shared/redux/store";
import { FC, PropsWithChildren } from "react";
import { Provider } from "react-redux";

type ReduxProviderProps = PropsWithChildren;
export const ReduxProvider: FC<ReduxProviderProps> = ({ children }) => {
  return <Provider store={store}>{children}</Provider>;
};
