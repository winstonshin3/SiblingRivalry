import {
  MainGameBoardWidget,
  SolveWidget,
  UserInputsWidget,
} from "@/widgets/siblingRivalry";
import { Box, VStack } from "@chakra-ui/react";

export const SiblingRivalryPage = () => {
  return (
    <Box height="100vh">
      <VStack spacing={3} align="stretch">
        <UserInputsWidget />
        <Box display="flex" justifyContent="center" alignItems="center" gap={3}>
          <MainGameBoardWidget />
        </Box>
        <SolveWidget />
      </VStack>
    </Box>
  );
};
