import { useSolveGame } from "@/features/solve-game";
import { Button } from "@chakra-ui/react";

export const SolveWidget = () => {
  const { isLoading, handleSolveClick } = useSolveGame();
  return (
    <Button
      size="lg"
      width="100%"
      colorScheme="teal"
      isLoading={isLoading}
      loadingText="Solving"
      onClick={handleSolveClick}
    >
      Solve!
    </Button>
  );
};
