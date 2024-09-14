import { INVADERS_LIST } from "@/entities/mechanics";
import { UnitCell, UnitCellGridItem } from "@/shared/ui";
import { Box, Grid, Heading } from "@chakra-ui/react";
import { DragEventHandler } from "react";

export const InvadersWidget = () => {
  const handleDragStart: DragEventHandler = (e) => {
    console.log("Invaders :: handleDragStart");
    const invaderTypeCode = (e.currentTarget as HTMLElement).dataset.typecode;
    if (!invaderTypeCode) {
      console.error("[InvadersWidget,handleDragStart] Got No Typecode");
      return;
    }
    e.dataTransfer.setData("typeCode", invaderTypeCode);
  };

  const handleDragEnd: DragEventHandler = (e) => {
    console.log("Invaders :: handleDragEnd");
  };
  return (
    <>
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
          p={4}
          minWidth={{ base: "520px", lg: "auto" }}
        >
          {INVADERS_LIST.map((invader, index) => {
            return (
              <UnitCellGridItem
                key={index}
                w="60px"
                h="60px"
                backgroundImage="/assets/Sprites/redtile.webp"
              >
                <UnitCell
                  invader={invader}
                  data-typecode={invader.typeCode}
                  onDragStart={handleDragStart}
                  onDragEnd={handleDragEnd}
                />
              </UnitCellGridItem>
            );
          })}
        </Grid>
      </Box>
    </>
  );
};
