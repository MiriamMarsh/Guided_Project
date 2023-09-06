// 
import { useEffect, useState } from "react";
import {useNavigate} from "react-router-dom";
const Login = () => {
    const [users, setUsers] = useState('')
    const [name, setName] = useState('')
    const [pass, setPass] = useState('')
    const navigate = useNavigate();
    const fetchUsers = async() => {
        try {
            const jsonUsers = await fetch('../users.json');
            const userlist = await jsonUsers.json();
            setUsers(userlist);
            console.log(users)
        }
        catch {
            console.log('error')
        }
    }
    useEffect(() =>
        {
            fetchUsers()
        },[])
    const checkLogin =() => {
        let findUser = users.find(e => e.name == name && e.pass == pass);
        if(findUser)
            {
                navigate('./store')
            }
        else alert('Incorrect name or password. Please try again.')
    }
    return (
    <>
    <div style={{ margin:'20% auto', width:200, border:'black solid 5px', paddingBottom:20, borderRadius:20, textAlign:'center'}}>
        <br /><input placeholder='Username' onChange={(e) => {setName(e.target.value)}}></input>
        <br /><br /><input placeholder='Password' onChange={(e) => {setPass(e.target.value)}}></input>
        <br /><br /><button style={{width:'170px'}} onClick={checkLogin}>Login</button>
    </div>
    </>)
}
export default Login;














