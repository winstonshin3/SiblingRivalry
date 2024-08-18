import {
  MainGameBoardWidget,
  SolveWidget,
  UserInputsWidget,
} from "@/widgets/siblingRivalry";
import { Box, Center, VStack } from "@chakra-ui/react";

export const SiblingRivalryPage = () => {
  return (
    <Box height="100vh" width="100wh" overflow="scroll">
      <Center>
        <VStack spacing={3} align="stretch" maxWidth="667px">
          <UserInputsWidget />
          <Box
            display="flex"
            justifyContent="center"
            alignItems="center"
            gap={3}
          >
            <MainGameBoardWidget />
          </Box>
          <SolveWidget />
        </VStack>
      </Center>
    </Box>
  );
};
