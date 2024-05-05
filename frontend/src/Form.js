import { useState } from 'react';
import './Form.css';

function Form() {
  const [form, setForm] = useState({
    pregnancies: "",
    glucose: "",
    blood_pressure: "",
    skin_thickness: "",
    insulin_level: "",
    bmi: "",
    diabetes_pedigree: "",
    age: "",
  });
// fetch data
  const handleSubmit = (event) => {
    event.preventDefault();

    const form_data = new FormData();
    //append form inputs
    form_data.append("1", form.pregnancies);
    form_data.append("2", form.glucose);
    form_data.append("3", form.blood_pressure);
    form_data.append("4", form.skin_thickness);
    form_data.append("5", form.insulin_level);
    form_data.append("6", form.bmi);
    form_data.append("7", form.diabetes_pedigree);
    form_data.append("8", form.age);
    
    fetch('http://localhost:3000 ',{
      method:'POST',
      body: form_data
    })
    .then(response => console.log(response))

  };

  const onChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setForm({ ...form, [name]: value });
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <h4 className="form-title">Diabetes Prediction Model</h4>
        {/* <p> Example to Predict Probability of Diabetes</p> */}
        <input
          type="number"
          name="pregnancies"
          onChange={onChange}
          placeholder="Number of Pregnancies"
          className="form-input"
        />
        <input
          type="number"
          name="glucose"
          onChange={onChange}
          placeholder="Glucose Level"
          className="form-input"
        />
        <input
          type="number"
          name="blood_pressure"
          onChange={onChange}
          placeholder="Blood Pressure"
          className="form-input"
        />
        <input
          type="number"
          name="skin_thickness"
          onChange={onChange}
          placeholder="Skin Thickness"
          className="form-input"
        />
        <input
          type="number"
          name="insulin_level"
          onChange={onChange}
          placeholder="Insulin Level"
          className="form-input"
        />
        <input
          type="number"
          name="bmi"
          onChange={onChange}
          placeholder="BMI (Body Mass Index)"
          className="form-input"
        />
        <input
          type="number"
          name="diabetes_pedigree"
          onChange={onChange}
          placeholder="Diabetes Pedigree Function"
          className="form-input"
        />
        <input
          type="number"
          name="age"
          onChange={onChange}
          placeholder="Age"
          className="form-input"
        />
        <button type="submit" className="form-button">Submit Form</button>
      </form>
    </div>
  );
}

export default Form;
