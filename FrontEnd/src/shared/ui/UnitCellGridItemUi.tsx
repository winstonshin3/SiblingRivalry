import { GridItem, GridItemProps } from "@chakra-ui/react";
import { FC } from "react";

type UnitCellGridItem = GridItemProps & {};
export const UnitCellGridItem: FC<UnitCellGridItem> = ({
  children,
  ...restProps
}) => {
  return (
    <GridItem
      backgroundSize="cover"
      backgroundPosition="center"
      backgroundRepeat="no-repeat"
      display="flex"
      justifyContent="center"
      alignItems="center"
      {...restProps}
    >
      {children}
    </GridItem>
  );
};
