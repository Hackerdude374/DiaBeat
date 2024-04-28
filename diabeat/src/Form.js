import {useState} from 'react';


function Form(){
const [form,  setForm] = useState({name: "", email: ""});
    const handleSubmit = (event)=>{
        event.preventDefault();

        console.log("form submitted");
        console.log(form);
    };

    const onChange = (event)=>{
        console.log("changed input field");
        const name = event.target.name;
        const value = event.target.value;

    console.log(`event.target.name: ${name}, event.target.value: ${value}`);

    setForm({...form, [name]: value});
    }

    return(
       <form onSubmit = {handleSubmit}>
        <input type = "text" name = "name"  onChange={onChange} placeholder = "Name (e.g. John)" />    
        <input type = "email" name = "email"  onChange={onChange} placeholder = "email (john doe@example.com)" />    
          <button type = "submit">Submit Form</button>
       </form>
    )
}

export default Form;