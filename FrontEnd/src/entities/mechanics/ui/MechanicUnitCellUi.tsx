import { Box, HTMLChakraProps } from "@chakra-ui/react";
import { Invader } from "../types/invader";
import { DragEventHandler, FC } from "react";

type MechanicUnitCellProps = HTMLChakraProps<"div"> & {
  invader: Invader;
};
export const MechanicUnitCell: FC<MechanicUnitCellProps> = ({
  invader,
  ...restProps
}) => {
  const handleDragStart: DragEventHandler = (e) => {
    console.log("Invaders :: handleDragStart");
    e.dataTransfer.setData("typeCode", invader.typeCode);
  };

  const handleDragEnd: DragEventHandler = (e) => {
    console.log("Invaders :: handleDragEnd");
  };

  return (
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
      backgroundColor="none"
      onDragStart={handleDragStart}
      onDragEnd={handleDragEnd}
      {...restProps}
    >
      {invader.typeCode}
    </Box>
  );
};
