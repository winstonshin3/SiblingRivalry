import { Grid, GridItem, Heading, VStack } from "@chakra-ui/react";

export const MainGameBoardWidget = () => {
  return (
    <>
      <VStack align="stretch">
        <Heading as="h3" size="md" textAlign="center" width="100%">
          Main Game Board
        </Heading>
        <Grid templateColumns="repeat(5, 1fr)" gap={2} p={4} bg="purple.900">
          {[...Array(40)].map((_, index) => {
            const isEven = index % 2 === 0;
            return (
              <GridItem
                key={index}
                w="60px"
                h="60px"
                bg={isEven ? "gray.600" : "purple.700"}
                border="1px"
                borderColor={isEven ? "gray.500" : "purple.600"}
              />
            );
          })}
        </Grid>
      </VStack>
      <VStack>
        <Heading as="h3" size="md" textAlign="center" width="100%">
          Invaders
        </Heading>
        <Grid templateColumns="repeat(1, 1fr)" gap={2} p={4} bg="purple.900">
          {[...Array(8)].map((_, index) => {
            return (
              <GridItem
                key={index}
                w="60px"
                h="60px"
                bg={"gray.600"}
                border="1px"
                borderColor={"gray.500"}
              />
            );
          })}
        </Grid>
      </VStack>
    </>
  );
};
