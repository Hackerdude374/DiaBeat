
function User(props){
    console.log(props);
    return(
        <h1>Name : {props.name} - Age: {props.age}</h1>
    );
}

function SecondUser(){
    return(
        <h2>second u ser data </h2>
    )
}



export { User, SecondUser };
