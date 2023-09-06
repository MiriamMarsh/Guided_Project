import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import {addtoCart} from "../features/cart_slice";
import {useDispatch} from "react-redux";
const Books = (props) => {
    const navigate = useNavigate();
    const dispatch = useDispatch () ;
    //const [books, setBooks] = useState([]);
    let book = props.book
    // useEffect(() => {
    //     getAllBooks()
    // }, [])
    // const [data, setData] = useState([]);
    // useEffect(() => {
    //     localStorage.setItem('currentBook', JSON.stringify(data));
    //   }, [data]);
    // let jsonFile = [];
    // const getAllBooks = async () => {
    //             console.log("in getAllBooks");
    //             let res = await fetch("../public/books.json");
    //             let jsonFile = await res.json();
    //             setBooks(jsonFile);
    //             console.log("books",book);
        // }
        const getBookDetails =  (id) => {
                // let index = books.findIndex(x => (x.id === id) );
                // console.log(books);
                localStorage.setItem('currentBookObj', JSON.stringify(book));
                console.log('in getBookDetails',book)
                navigate('/bookdisplay');
            }
            const addBook = () => {
                dispatch(addtoCart({book}))
            }
 return(
    <>
    <h2>{props.book.title}</h2>
    <button onClick={() =>getBookDetails()}><img src={require(`../images/${props.book.img}`)}></img></button>
    <button onClick={() =>addBook()}>Add to Cart:</button>
    </>
 )
}
export default Books