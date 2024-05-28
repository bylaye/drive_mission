// src/Missions.js
import axios from 'axios';
import React, { useState } from 'react';

const Missions = () => {
  const [formData, setFormData] = useState({
    typeMission: '',
    statusMission: '',
    description: '',
    debutMission: '',
    finMission: '',
    quantite: 0,
  });

  const [message, setMessage] = useState('')
  
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      await axios.post('http://localhost:8000/missions/add',
        {...formData,
          finMission: formData.finMission ? formData.finMission : null,
        },
        {headers:{'Content-Type': 'application/json',}},
      );
      setMessage(`Mission : bien ajouté`)
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
            <label>Type de Mission:</label>
            <input 
              required
              type="text"
              name='typeMission'
              value={formData.typeMission}
              onChange={handleChange} 
            />
          </div>

          <div>
            <label>Description:</label>
            <input 
              required
              type="text"
              name='description' 
              value={formData.description}
              onChange={handleChange}
            />
          </div>

          <div>
            <label>Date de début:</label>
            <input
              required
              type="date"
              name='debutMission'
              value={formData.debutMission}
              onChange={handleChange}
            />
          </div>

          <div>
            <label>Date de fin:</label>
            <input
              type="date" 
              name='finMission'
              value={formData.finMission}
              onChange={handleChange}
            />
          </div>
          
          <div>
            <label>Status Mission:</label>
            <input
              required
              type="text"
              value={formData.statusMission}
              name='statusMission'
              onChange={handleChange}
            />
          </div>

          <div>
            <label>Quantite:</label>
            <input
              required
              type="number"
              name='quantite'
              value={formData.quantite}
              onChange={handleChange}
            />
          </div>

          <button type="submit">Soumettre</button>
        </form>
      )}
    </div>
  );
};

export default Missions;
