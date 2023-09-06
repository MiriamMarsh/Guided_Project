// import {useEffect, useState} from 'react';
// import {useNavigate} from 'react-router-dom';

// const Login = () => {
//     let users= [];
//     const [name,setname] = useState("");
//     const [pass,setpass] = useState("");
//     const navigate = useNavigate()  ;
//     const fetchUser = async () =>{
//         let res = await fetch("user.json");
//         users = await res.json(); 
//         console.log(users);
//         // checkUser(),[]
// }
    
//     // useEffect(() => {
//     //     getBooks()}
//     //     ,[])
//     // const getIndexOfUser = () => {
//     //     return users.findIndex(x => (x.username === name) && (x.password === pass));

//     const checkUser = () => { 
        
//         console.log(name,pass);
//         let findUser = users.find(e => e.name === name && e.pass === pass);
//         if (findUser) {
//             navigate('./Store')
//         }
//         else {
//             navigate('Sorry, this site is only for registered users. Please contact admin')
//         }
//     }
//     fetchUser();
// return (
//         <>
//             <h2>Please enter your username and password.</h2>
//             <div style={{ backgroundColor: 'teal' }}>
//                 <input placeholder="username" onChange={(e) => setname(e.target.value)}></input><br></br>
//                 <input placeholder="password" onChange={(e) => setpass(e.target.value)}></input><br></br>
//                 <button onClick={checkUser}> submit</button>
//             </div>
//         </>
//     )
// }
// export default Login;   

