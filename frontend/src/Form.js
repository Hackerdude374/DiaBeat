import React, { useState } from 'react';
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
  const [result, setResult] = useState(""); // result display
  const [showResult, setShowResult] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();

    const form_data = new FormData();
    form_data.append("1", form.pregnancies);
    form_data.append("2", form.glucose);
    form_data.append("3", form.blood_pressure); // Changed from blood_presure
    form_data.append("4", form.skin_thickness);
    form_data.append("5", form.insulin_level);
    form_data.append("6", form.bmi);
    form_data.append("7", form.diabetes_pedigree);
    form_data.append("8", form.age);

    fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: form_data
    })
    .then(response => response.text()) // Assuming response is JSON
    .then(html =>{
      setResult(html);
      setShowResult(true);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  const onChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setForm({ ...form, [name]: value });
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = (e) => {
      const content = e.target.result;
      const lines = content.split('\n');
      const values = {};

      lines.forEach(line => {
        const [key, value] = line.split('=').map(part => part.trim().toLowerCase());
        values[key] = value;
      });

      setForm({
        pregnancies: values.pregnancies || "",
        glucose: values.glucose || "",
        blood_pressure: values.blood_pressure || "",
        skin_thickness: values.skin_thickness || "",
        insulin_level: values.insulin_level || "",
        bmi: values.bmi || "",
        diabetes_pedigree: values.diabetes_pedigree || "",
        age: values.age || "",
      });
    };

    if (file) {
      reader.readAsText(file);
    }
  };

  const closePopup = () => {
    setShowResult(false);
  };

  return (
    <div className="form-container">
      <form onSubmit={handleSubmit}>
        <h4 className="form-title">Diabeat: The #1 Diabetes Prediction Model</h4>
        <div className="form-column">
          <input
            type="number"
            name="pregnancies"
            onChange={onChange}
            value={form.pregnancies}
            placeholder="Number of Pregnancies"
            className="form-input"
          />
          <input
            type="number"
            name="glucose"
            onChange={onChange}
            value={form.glucose}
            placeholder="Glucose Level"
            className="form-input"
          />
          <input
            type="number"
            name="blood_pressure"
            onChange={onChange}
            value={form.blood_pressure}
            placeholder="Blood Pressure"
            className="form-input"
          />
          <input
            type="number"
            name="skin_thickness"
            onChange={onChange}
            value={form.skin_thickness}
            placeholder="Skin Thickness"
            className="form-input"
          />
        </div>
        <div className="form-column">
          <input
            type="number"
            name="insulin_level"
            onChange={onChange}
            value={form.insulin_level}
            placeholder="Insulin Level"
            className="form-input"
          />
          <input
            type="text"
            name="bmi"
            onChange={onChange}
            value={form.bmi}
            placeholder="BMI (Body Mass Index)"
            className="form-input"
          />
          <input
            type="text"
            name="diabetes_pedigree"
            onChange={onChange}
            value={form.diabetes_pedigree}
            placeholder="Diabetes Pedigree Function"
            className="form-input"
          />
          <input
            type="number"
            name="age"
            onChange={onChange}
            value={form.age}
            placeholder="Age"
            className="form-input"
          />
        </div>
        <div className="form-column">
          <input
            type="file"
            onChange={handleFileUpload}
            accept=".txt"
            className="form-input"
          />
        </div>
        <button type="submit" className="form-button">Submit Form</button>
      </form>
      {showResult && (
        <div className="backdrop" onClick={closePopup}>
          <div className="result-popup">
            <button className="close-button" onClick={closePopup}>×</button>
            <div dangerouslySetInnerHTML={{ __html: result }} className="result" />
          </div>
        </div>
      )}
    </div>
  );
}

export default Form;
