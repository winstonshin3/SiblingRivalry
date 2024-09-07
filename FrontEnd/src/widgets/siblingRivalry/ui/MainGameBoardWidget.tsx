import { Invader, INVADERS_LIST, MechanicUnitCell } from "@/entities/mechanics";
import { Box, Grid, GridItem, Heading, HStack, VStack } from "@chakra-ui/react";
import { DragEventHandler, useState } from "react";

export const MainGameBoardWidget = () => {
  const [gameBoard, setGameBoard] = useState<Array<Invader | null>>(
    Array.from({ length: 40 }, () => null)
  );

  const handleDragOver: DragEventHandler = (e) => {
    e.preventDefault();
  };

  const handleDragEnter: DragEventHandler = (e) => {
    console.log("handleDragEnter");
  };

  const handleDrop: DragEventHandler = (e) => {
    const currentIndex = parseInt(
      (e.target as HTMLElement).dataset.index ?? "-1"
    );

    if (currentIndex === -1) {
      console.error("currentIndex -1인디요;");
      return;
    }

    const invaderTypeCode = e.dataTransfer.getData("typeCode");
    const invaderObjectToAdd = INVADERS_LIST.find(
      (invader) => invader.typeCode === invaderTypeCode
    );

    if (!invaderObjectToAdd) {
      console.error("invaderObjectToAdd가 없대요;");
      return;
    }

    setGameBoard((prev) => [
      ...prev.slice(0, currentIndex),
      invaderObjectToAdd,
      ...prev.slice(currentIndex + 1, prev.length),
    ]);
  };

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
          {gameBoard.map((invader, index) => {
            const isEven = index % 2 === 0;
            return (
              <GridItem
                key={index}
                w="60px"
                h="60px"
                bg={isEven ? "gray.600" : "purple.700"}
                border="1px"
                borderColor={isEven ? "gray.500" : "purple.600"}
                display="flex"
                justifyContent="center"
                alignItems="center"
                data-index={index}
                onDragOver={handleDragOver}
                onDragEnter={handleDragEnter}
                onDrop={handleDrop}
              >
                <Box
                  as="span"
                  draggable
                  w="100%"
                  h="100%"
                  display="flex"
                  justifyContent="center"
                  alignItems="center"
                  userSelect="none"
                  cursor="move"
                  data-index={index}
                >
                  {invader?.typeCode}
                </Box>
              </GridItem>
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
