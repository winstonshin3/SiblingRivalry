import { useAppDispatch, useAppSelector } from "@/shared/redux/hooks";
import { INVADERS_LIST, setGameBoard } from "@/entities/mechanics";
import { Grid, Heading } from "@chakra-ui/react";
import { DragEventHandler } from "react";
import { UnitCell, UnitCellGridItem } from "@/shared/ui";

export const MainGameBoardWidget = () => {
  // const [gameBoard, setGameBoard] = useState<Array<Invader | null>>(
  //   Array.from({ length: 40 }, () => null)
  // );

  const gameBoard = useAppSelector((state) => state.gameBoard.value);
  const dispatch = useAppDispatch();

  console.debug("gameBoard", gameBoard);

  const handleDragOver: DragEventHandler = (e) => {
    e.preventDefault();
  };

  const handleDrop: DragEventHandler = (e) => {
    e.preventDefault();
    const currentIndex = parseInt(
      (e.currentTarget as HTMLElement).dataset.index ?? "-1"
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

    dispatch(
      setGameBoard([
        ...gameBoard.slice(0, currentIndex),
        { ...invaderObjectToAdd, onBoardStatus: "on" },
        ...gameBoard.slice(currentIndex + 1, gameBoard.length),
      ])
    );
  };

  return (
    <>
      <Heading as="h3" size="md" textAlign="center" width="100%">
        Main Game Board
      </Heading>
      <Grid templateColumns="repeat(5, 1fr)" p={4} bg="purple.900">
        {gameBoard.map((invader, index) => {
          const isEven = index % 2 === 0;
          return (
            <UnitCellGridItem
              key={index}
              w="60px"
              h="60px"
              backgroundImage={`/assets/Sprites/${
                isEven ? "redtile" : "graytile"
              }.webp`}
              data-index={index}
              onDragOver={handleDragOver}
              onDrop={handleDrop}
              opacity={invader?.onBoardStatus === "hover" ? 0.5 : 1}
            >
              <UnitCell invader={invader} />
            </UnitCellGridItem>
          );
        })}
      </Grid>
    </>
  );
};
