// src/Missions.js
import axios from 'axios';
import React, { useState } from 'react';

const Partenaires = () => {
  const [formData, setFormData] = useState({
    nomPartenaire: '',
    adressePartenaire: '',
    emailPartenaire: '',
    telephonePartenaire: '',
    
  });

  const [message, setMessage] = useState('')
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      await axios.post('http://localhost:8000/partenaires/add',
        {...formData,
        },
        {headers:{'Content-Type': 'application/json',}},
      );
      setMessage(`Partenaire : bien ajouté`)
      console.log(formData)
    }catch (error){
      console.log('Error', error)
      if (error.message === 'Network Error') {
        setMessage('Erreur réseau');
      }
      else if (error.response && error.response.data && error.response.data.detail){
        setMessage(error.response.data.detail)
      }
      else{
        setMessage("Erreur: UNKNOWN")
      }
    }
  };


  return (
    <div>
      <h1>Missions</h1>
      <div className='message'>
        {
          message && 
          <p 
          className={message ? (message.includes('bien ajouté') ? 'valid' : 'invalid') : ''}
          >
            {message} 
          </p>}
      </div>
      {formData && (
        <form onSubmit={handleSubmit}>
          <div>
            <label>Nom Partenaire:</label>
            <input 
              required
              type="text"
              name='nomPartenaire'
              value={formData.nomPartenaire}
              onChange={handleChange}
            />
          </div>

          <div>
            <label>Adresse:</label>
            <input 
              required
              type="text"
              name='adressePartenaire'
              value={formData.adressePartenaire}
              onChange={handleChange} 
            />
          </div>

          <div>
            <label>Telephone:</label>
            <input 
              required
              type="text"
              name='telephonePartenaire' 
              value={formData.telephonePartenaire}
              onChange={handleChange}
            />
          </div>

          <div>
            <label>Email:</label>
            <input
              required
              type="email"
              name='emailPartenaire'
              value={formData.emailPartenaire}
              onChange={handleChange}
            />
          </div>

          <button type="submit">Soumettre</button>
        </form>
      )}
    </div>
  );
};

export default Partenaires;
