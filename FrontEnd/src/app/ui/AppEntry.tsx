import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "../styles/index.css";
import { SiblingRivalryPage } from "@/pages/siblingRivalry";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <SiblingRivalryPage />
  </StrictMode>
);
