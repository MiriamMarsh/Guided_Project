import {useSelector, useDispatch} from "react-redux"
import { useNavigate } from "react-router-dom"


export default function ShoppingCart ()
{
const cart = useSelector((state) => state.cartSlice.cart);
const total = useSelector((state) => state.cartSlice.price);
const navigate = useNavigate();
console.log('total:', total);

return(
    <div style={{ minWidth: '60%', textAlign: 'center', backgroundColor: 'pink', margin: '50px', padding: '35px', borderRadius:20 }}>
        <h2>Shopping Cart</h2>
        {cart.map((e,index) => (
            <>
            <div style = {{display:'flex', justifyContent:'space-between'}}>
                <span style={{width:'60%', textAlign:'left'}}>{e.title}</span>
                <span>${e.price}</span>
            </div>
            </>
            ))}
            <h4 style={{textAlign:'right'}}>Total: ${total}</h4>
            <button onClick={()=>navigate('/store')}>Continue Shopping</button>
    </div>
    )
}
