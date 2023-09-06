import { configureStore} from '@reduxjs/toolkit';
// import counterSlice from '../features/counterSlice';
import cartSlice from '../features/cart_slice';
export const redux_store = configureStore({
    reducer: {cartSlice}
})