import {
  MainGameBoardWidget,
  SolveWidget,
  UserInputsWidget,
} from "@/widgets/siblingRivalry";
import { Box, Center, VStack } from "@chakra-ui/react";

export const SiblingRivalryPage = () => {
  return (
    <Box height="100vh" width="100wh">
      <Center>
        <VStack spacing={3} align="stretch" maxWidth="667px" overflow="auto">
          <UserInputsWidget />
          <Box>
            <MainGameBoardWidget />
          </Box>
          <SolveWidget />
        </VStack>
      </Center>
    </Box>
  );
};
