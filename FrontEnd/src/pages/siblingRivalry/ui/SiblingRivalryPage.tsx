import {
  InvadersWidget,
  MainGameBoardWidget,
  SolveWidget,
  UserInputsWidget,
} from "@/widgets/siblingRivalry";
import { Box, Center, HStack, VStack } from "@chakra-ui/react";

export const SiblingRivalryPage = () => {
  return (
    <Box
      height="100vh"
      width="100wh"
      backgroundImage={
        "url('https://static.wikia.nocookie.net/necromerger/images/0/08/Site-background-dark')"
      }
      color={"white"}
      backgroundSize={"310px auto"}
      backgroundAttachment={"fixed"}
      style={{ imageRendering: "pixelated" }}
    >
      <Center height="100vh">
        <VStack
          backgroundColor="#1e0c1b"
          className="main_page"
          minHeight={"480px"}
          // TODO: 스타일은 나중에 먹이기
          // style={{
          //   borderImageOutset: "20px 20px 5px 20px",
          //   borderRadius: "3px 0 0 3px",
          //   borderImageSlice: "20 fill",
          //   borderImageWidth: "40px",
          //   borderImageSource:
          //     'url("https://static.wikia.nocookie.net/necromerger/images/e/e2/PanelBacking_Dark.png")',
          // }}
          spacing={3}
          align="stretch"
          maxWidth="667px"
          overflow="auto"
          padding={"24px 36px"}
          as="main"
        >
          <UserInputsWidget />
          <Box>
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
                <MainGameBoardWidget />
              </VStack>
              <VStack
                align="stretch"
                width={{ base: "full", lg: "auto" }}
                maxWidth="400px"
              >
                <InvadersWidget />
              </VStack>
            </HStack>
          </Box>
          <SolveWidget />
        </VStack>
      </Center>
    </Box>
  );
};
