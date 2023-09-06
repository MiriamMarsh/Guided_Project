import React from 'react';
import Login from './components/login2';
import BookStore from './components/store';
import BookDetails from './components/bookdetails';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Provider } from 'react-redux';
import { redux_store } from './redux/redux_store';
import ShoppingCart from './components/shopping_cart';


function App() {
  return (
    <>
    <Provider store ={redux_store}>
      <BrowserRouter>
      <Routes>
          <Route path='/' element={<Login></Login>}></Route>
          <Route path='/store' element={<BookStore></BookStore>}></Route>
          <Route path='/bookdisplay' element={<BookDetails></BookDetails>}></Route>
          <Route path='/shopping_cart' element={<ShoppingCart></ShoppingCart>}></Route>

      </Routes>
      </BrowserRouter>
      </Provider>
    </>
  );
}
export default App;









