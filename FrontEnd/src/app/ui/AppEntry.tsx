import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { SiblingRivalryPage } from "@/pages/siblingRivalry";
import { ChakraProvider } from "@chakra-ui/react";

/**
 * {1} : TODO: change ChakraProvider to ChakraBaseProvider for JS payload https://v2.chakra-ui.com/getting-started#chakrabaseprovider
 */

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    {/* {1} */}
    <ChakraProvider>
      <SiblingRivalryPage />
    </ChakraProvider>
  </StrictMode>
);
