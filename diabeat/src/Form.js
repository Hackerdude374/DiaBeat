function Form(){

    const handleSubmit = (event)=>{
        event.preventDefault();
        console.log("form submitted");

    };
    return(
       <form onSubmit = {handleSubmit}>
        <button type = "submit">Submit Form</button>
       </form>
    )
}

export default Form;