import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { Invader } from "../types/invader";
import { RootState } from "@/shared/redux/store";

export interface GameBoardState {
  value: Array<Invader | null>;
}

const initialState: GameBoardState = {
  value: Array.from({ length: 40 }, () => null),
};

const gameBoardSlice = createSlice({
  name: "gameBoard",
  initialState,
  reducers: {
    setGameBoard: (state, action: PayloadAction<Array<Invader | null>>) => {
      state.value = action.payload;
    },
  },
});

export const { setGameBoard } = gameBoardSlice.actions;
export const selectGameBoard = (state: RootState) => state.gameBoard.value;
export const gameBoardReducer = gameBoardSlice.reducer;
