import React, { useState, useRef } from 'react';
import "./App.css";
import axios from 'axios';




function App() {
  const CreateUserRef = useRef()
  const CreateTweetRef = useRef()

  const [name, setName] = useState("")
  const [password, setPassword] = useState("")
  const [email, setEmail] = useState("")
  const [tweet, setTweet] = useState("")
  const [username, setUsername] = useState("")

  let headers = { mode: 'no-cors' }

  const GetFollowingTweets = () => {
    axios.get("http://localhost:5000/see_tweets").then((response) => {
      console.log("got response ---" + response.data)
    });
  };


  const MakeTweet = () => {
    console.log("got ---", username, tweet)
    axios.post("http://localhost:5000/tweet", {
      username: username,
      tweet: tweet,
    }, headers).then((response) => {
      console.log("got response ---" + response.data)
      alert(response.data)
    });
  };

  const CreateUser = () => {
    console.log("got ---", name, password, email)
    axios.post("http://localhost:5000/create_user", {
      username: name,
      password: password,
      email: email,
    }, headers).then((response) => {
      console.log("got response ---" + response.data)
      alert(response.data)
    });
  };

  const Login = () => {
    console.log("got ---", name, password)
    axios.post("http://localhost:5000/login", {
      username: name,
      password: password,
    }).then((response) => {
      console.log("got response ---" + response.data)
      alert(response.data)
    });
  };


  return (
    <div className="App">
      <h1> <center>Welcome to Twitter</center> </h1>
      <div className="form">
        <h2> Create Account</h2>
        <label> Username </label>
        <input ref={CreateUserRef} type="text" name="Username"
          onChange={(event) => { setName(event.target.value) }} />
        <label> Password </label>
        <input ref={CreateUserRef} type="password" name="Password"
          onChange={(event) => { setPassword(event.target.value) }} />
        <label> Email </label>
        <input ref={CreateUserRef} type="text" name="Email"
          onChange={(event) => { setEmail(event.target.value) }} />
        <button onClick={CreateUser}> Create Account </button>

        <div className="login">
          <h2> Login</h2>
          <input ref={CreateUserRef} type="text" placeholder="Username"
            onChange={(event) => { setName(event.target.value) }} />
          <input ref={CreateUserRef} type="password" placeholder="Password"
            onChange={(event) => { setPassword(event.target.value) }} />
          <button onClick={Login}> Login </button>
        </div>


        <div className="login">
          <h2> Tweets</h2>
          {/* <button onClick={GetTweets}> See Tweets </button> */}
          <label> Message </label> 
          <input ref={CreateTweetRef} type="text" name = "Message"
            onChange={(event) => {setTweet(event.target.value)}} />
          <label> Username </label> 
          <input ref={CreateTweetRef} type="text" name = "Message"
            onChange={(event) => {setUsername(event.target.value)}} />
          <button onClick={MakeTweet}> Post Tweet </button>
          
        </div>


        <div className="follow">
          <h2> Follow Other Users </h2>
          <button onClick={GetFollowingTweets}> Follow </button>
        </div>




      </div>
    </div>

  );
}

export default App;