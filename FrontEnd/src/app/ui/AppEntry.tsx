import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { SiblingRivalryPage } from "@/pages/siblingRivalry";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <SiblingRivalryPage />
  </StrictMode>
);
