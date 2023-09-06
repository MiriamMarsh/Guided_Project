import { useNavigate } from "react-router-dom";
import Books from "./books";
import { useEffect, useState } from "react";


const BookStore = () => {
    const [books, setBooks] = useState([]);
    const navigate = useNavigate()
    useEffect(() => {
        getAllBooks()
    }, [])
    const getAllBooks = async () => {
        console.log("in getAllBooks")
        let res = await fetch("../books.json");
        let jsonFile = await res.json();
        setBooks(jsonFile);
        console.log("books", books);
    }
    return (
        <>
                <h1>Welcome to our Store:</h1>  
                <button onClick={()=>navigate('/shopping_cart')}>View Cart</button>
          {
                books.map((e, index) => (
                    <Books book={e} key={index}></Books>
                ))
            }
        </>
    )
}
export default BookStore;

