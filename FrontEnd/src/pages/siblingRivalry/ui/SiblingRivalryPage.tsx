import { UserInputsWidget } from "@/widgets/siblingRivalry";
import { Box, VStack } from "@chakra-ui/react";

export const SiblingRivalryPage = () => {
  return (
    <Box height="100vh">
      <VStack spacing={4} align="stretch">
        <UserInputsWidget />
      </VStack>
    </Box>
  );
};
