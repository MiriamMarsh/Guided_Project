import {createSlice} from '@reduxjs/toolkit'

const cartSlice = createSlice ({
    name:'cart',
    initialState: {cart:[], price:0},
    reducers: {
        addtoCart: (state,actions) =>{state.cart.push(actions.payload.book);
        state.price += actions.payload.book.price;
        }
    }

})
export default cartSlice.reducer;
export const {addtoCart} = cartSlice.actions;
