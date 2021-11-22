import React, { useState, useRef} from 'react';
import "./App.css";
import axios from 'axios';


function App() {
  const CreateUserRef = useRef()

  const [name, setName] = useState("")
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [UserList, setUserList] = useState([])

 
 
  const CreateUser = () => {
    axios.post("http://localhost:5000/create_user", {
      username: name,
      userPassword: password,
      email: email,
    }).then(() => {
      setUserList([
        ...UserList,
        {
          username: name,
          userPassword: password,
          email: email
        },
      ]);
    });
  };
  
 


  return (
    <div className="App">
      <h1> <center>Twitter</center> </h1>

      <div className="form">
      <h2> Create Account</h2>
        <label> Username </label>
        <input ref={CreateUserRef} type="text" name="Username"
          onChange={(event) => {setName(event.target.value) }} />
        <label> Password </label>
        <input ref={CreateUserRef} type="password" name="Password"
          onChange={(event) => {setPassword(event.target.value) }} />
        <label> Email </label>
        <input ref={CreateUserRef} type="text" name="Email"
          onChange={(event) => {setEmail(event.target.value) }} />
       
        <button onClick={CreateUser}> Create Account </button>
      </div>
     </div>

  );
}

export default App;