import { createRoot } from "react-dom/client";
import { SiblingRivalryPage } from "@/pages/siblingRivalry";
import { ChakraProvider } from "@chakra-ui/react";
import { ReduxProvider } from "../providers/ReduxProvider";

/**
 * {1} : TODO: change ChakraProvider to ChakraBaseProvider for JS payload https://v2.chakra-ui.com/getting-started#chakrabaseprovider
 */

createRoot(document.getElementById("root")!).render(
  /* {1} */
  <ChakraProvider>
    <ReduxProvider>
      <SiblingRivalryPage />
    </ReduxProvider>
  </ChakraProvider>
);
