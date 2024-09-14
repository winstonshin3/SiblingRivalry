import { gameBoardReducer } from "@/entities/mechanics";
import { configureStore } from "@reduxjs/toolkit";

export const store = configureStore({
  reducer: {
    // 여기에 리듀서들을 추가합니다
    gameBoard: gameBoardReducer,
  },
});

// Infer the `RootState`,  `AppDispatch`, and `AppStore` types from the store itself
export type RootState = ReturnType<typeof store.getState>;
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch;
export type AppStore = typeof store;
