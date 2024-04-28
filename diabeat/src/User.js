import {useState} from 'react';
function User(props){
    console.log(props);
    return(
        <h1>Name : {props.name} - Age: {props.age}
        <button onClick={props.function}>Click Me</button>
        
        
        </h1>
    );
}

function SecondUser(){
   const [counter, setCounter] = useState(0);
    const increment = () =>{
        //update state of the component
        setCounter(counter +1);
    }
    return(
        <div>
        <h2>second u ser data </h2>
        <button onClick = {increment}> click  me</button>
        <p>you clicked the button {counter} times</p>

        </div>
    )
}



export { User, SecondUser };
