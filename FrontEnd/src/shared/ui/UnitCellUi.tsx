import { Invader } from "@/entities/mechanics";
import { Box, HTMLChakraProps } from "@chakra-ui/react";
import { FC } from "react";

// TODO: 타입이 여러개 더 생긴다면 T extends SomeType으로
type UnitCellProps = HTMLChakraProps<"div"> & {
  invader: Invader | null;
};
export const UnitCell: FC<UnitCellProps> = ({ invader, ...restProps }) => {
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
      {...restProps}
    >
      <img src={invader?.icon} alt={invader?.typeCode} />
    </Box>
  );
};
