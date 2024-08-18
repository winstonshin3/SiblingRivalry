import { FormControl, FormLabel, HStack, Input } from "@chakra-ui/react";
import { useId } from "react";

export const UserInputsWidget = () => {
  const id = useId();
  return (
    <HStack justifyContent="center" alignItems="center" flexWrap="wrap" p={4}>
      <HStack spacing={3}>
        <FormControl display="flex" alignItems="center" id={`score-${id}`}>
          <FormLabel mb={0} mr={2}>
            Score
          </FormLabel>
          <Input type="tel" placeholder="Score" size="sm" />
        </FormControl>
        <FormControl display="flex" alignItems="center" id={`ore-${id}`}>
          <FormLabel mb={0} mr={2}>
            Ore
          </FormLabel>
          <Input type="tel" placeholder="Ore" size="sm" />
        </FormControl>
      </HStack>
    </HStack>
  );
};
