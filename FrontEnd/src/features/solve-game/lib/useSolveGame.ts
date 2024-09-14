import { useAppSelector } from "@/shared/redux/hooks";
import { useCallback, useState } from "react";

export const useSolveGame = () => {
  // TODO: mocking loading state
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const gameBoard = useAppSelector((state) => state.gameBoard.value);

  const handleSolveClick = useCallback(() => {
    setIsLoading(true);
    console.debug("gameBoard", gameBoard);
    setTimeout(() => {
      setIsLoading(false);
    }, 2000);
  }, [gameBoard]);

  return {
    isLoading,
    handleSolveClick,
  };
};
