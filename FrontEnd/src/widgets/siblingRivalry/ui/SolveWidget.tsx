import { Button } from "@chakra-ui/react";
import { useCallback, useState } from "react";

export const SolveWidget = () => {
  // TODO: mocking loading state
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const handleSolveClick = useCallback(() => {
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
    }, 2000);
  }, []);
  return (
    <Button
      size="lg"
      width="100%"
      colorScheme="teal"
      isLoading={isLoading}
      loadingText="Solving..."
      onClick={handleSolveClick}
    >
      Solve!
    </Button>
  );
};
