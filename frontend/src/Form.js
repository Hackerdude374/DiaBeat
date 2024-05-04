import {useState} from 'react';


function Form(){
const [form,  setForm] = useState({ //input fields for form
    pregnancies:"",
    glucose:"",
    blood_pressure:"",
    skin_thickness:"",
    insulin_level:"",
    bmi:"",
    diabetes_pedigree:"",
    age:"",




});
    const handleSubmit = (event)=>{
        event.preventDefault();

        console.log("form submitted");
        console.log(form);
    };

    const onChange = (event)=>{
 
        const name = event.target.name;
        const value = event.target.value;



    setForm({...form, [name]: value});
    }
//form build
    return (
        <form onSubmit={handleSubmit}>

            <h4>Diabetes Prediction Model</h4>
            <p> Example to Predict Probability of Diabetes</p>
          <input
            type="number"
            name="pregnancies"
            onChange={onChange}
            placeholder="Number of Pregnancies"
          />
          <input
            type="number"
            name="glucose"
            onChange={onChange}
            placeholder="Glucose Level"
          />
          <input
            type="number"
            name="blood_pressure"
            onChange={onChange}
            placeholder="Blood Pressure"
          />
          <input
            type="number"
            name="skin_thickness"
            onChange={onChange}
            placeholder="Skin Thickness"
          />
          <input
            type="number"
            name="insulin_level"
            onChange={onChange}
            placeholder="Insulin Level"
          />
          <input
            type="number"
            name="bmi"
            onChange={onChange}
            placeholder="BMI (Body Mass Index)"
          />
          <input
            type="number"
            name="diabetes_pedigree"
            onChange={onChange}
            placeholder="Diabetes Pedigree Function"
          />
          <input
            type="number"
            name="age"
            onChange={onChange}
            placeholder="Age"
          />
          <button type="submit">Submit Form</button>
        </form>
      );
      
}

export default Form;