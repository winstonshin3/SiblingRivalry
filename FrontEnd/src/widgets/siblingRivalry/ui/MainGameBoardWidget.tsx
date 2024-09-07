import { Invader, INVADERS_LIST, MechanicUnitCell } from "@/entities/mechanics";
import { Box, Grid, GridItem, Heading, HStack, VStack } from "@chakra-ui/react";

export const MainGameBoardWidget = () => {
  return (
    <HStack
      spacing={3}
      justifyContent="center"
      alignItems="flex-start"
      flexWrap="wrap"
    >
      <VStack
        align="stretch"
        width={{ base: "full", lg: "auto" }}
        maxWidth="400px"
      >
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
      <VStack
        align="stretch"
        width={{ base: "full", lg: "auto" }}
        maxWidth="400px"
      >
        <Heading
          as="h3"
          size="md"
          textAlign={{ base: "left", lg: "center" }}
          width="100%"
        >
          Invaders
        </Heading>
        <Box
          overflowX="auto"
          width="100%"
          bg="purple.900"
          css={{
            "&::-webkit-scrollbar": {
              height: "8px",
            },
            "&::-webkit-scrollbar-track": {
              width: "6px",
              background: "black.800",
            },
            "&::-webkit-scrollbar-thumb": {
              background: "black.600",
              borderRadius: "24px",
            },
          }}
        >
          <Grid
            templateColumns={{
              base: `repeat(${INVADERS_LIST.length}, 60px)`,
              lg: "repeat(1, 60px)",
            }}
            gap={2}
            p={4}
            minWidth={{ base: "520px", lg: "auto" }}
          >
            {INVADERS_LIST.map((invader, index) => {
              return (
                <GridItem
                  key={index}
                  w="60px"
                  h="60px"
                  bg={"gray.600"}
                  border="1px"
                  borderColor={"gray.500"}
                  display="flex"
                  justifyContent="center"
                  alignItems="center"
                >
                  <MechanicUnitCell invader={invader} />
                </GridItem>
              );
            })}
          </Grid>
        </Box>
      </VStack>
    </HStack>
  );
};
