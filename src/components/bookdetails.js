import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
export default function BookDetails  () {
    let storage = localStorage.getItem("currentBookObj");
    console.log(storage);
    let book = JSON.parse(storage);
    console.log(book);

    const cart = () => {}

    return (

        <h1>
        <img src={require(`../images/${book.img}`)}></img>
        <br></br><u>Book Title: </u> {book.title}
        <br></br><u>Book Subtitle: </u>{book.subtitle}
        <br></br><u>Author: </u>{book.author}
        <br></br><u>Published: </u>{book.published}
        <br></br><u>Publisher: </u>{book.publisher}
        <br></br><u>Pages: </u>{book.pages}
        <br></br><u>Price: </u>{book.price}
        <br></br><u>Description: </u>{book.description}
        <button onClick= {cart}>Add to cart:</button>


        
        
        
        </h1>

    )

}
