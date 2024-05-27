// src/Chauffeurs.js
import axios from 'axios';
import React, { useState } from 'react';

const Chauffeurs = ({action}) => {
  const [formData, setFormData] = useState({
    codePermanent: '',
    prenom:'',
    nom:'',
    adresse: '',
    telephone: '',
    dateNaissance: '',
  });


  const [message, setMessage] = useState('')
  const [errors, setErrors] = useState({
    codePermanent:'Code Permanent au moins 6 caracteres',
  })

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));

    switch (name){
      case 'codePermanent':
        checkCodePermanent(value)
        break;
      default:
        break;
    }
  };


  const checkCodePermanent = async (value) => {
    try{
      if (value.length < 6) {
        setErrors((prev) => ({...prev, codePermanent: 'Code Permanent au moins 6 caracteres'}));
      }
      else{
        const response = await axios.get(`http://localhost:8000/chauffeurs/get/chauffeurs/codepermanent/${value}`);
        if (!response.data.exists){
          setErrors((prev) => ({...prev, codePermanent: 'Code Permanent deja utilise'}));        
        }
        else{
          setErrors((prev) => ({...prev, codePermanent: 'Code Permanent disponible'}));
        }
      }
    }catch (error) {
      if (value){
        setErrors((prev) => ({...prev, codePermanent: 'Code Permanent disponible'}));
      }
    }
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    try{
      const response = await axios.post('http://localhost:8000/chauffeurs/add',
        {...formData},
        {headers:{'Content-Type': 'application/json',}},
      );
      console.log(response)
      setMessage(`Chauffeur ${response.data.codePermanent} : ${response.data.prenom} bien ajouté`)
      setFormData({
        codePermanent:'',
        prenom: '',
        nom: '',
        adresse:'',
        telephone: '',
        dateNaissance:'',
      })
      setErrors((prev) => ({...prev, codePermanent: ''}));
    }catch (error) {
      if (error.message === 'Network Error') {
        setMessage('Erreur réseau : Impossible de se connecter');
      }
      else if (error.response && error.response.data && error.response.data.detail){
        setMessage(error.response.data.detail)
      }
      else{
        setMessage("Erreur: UNKNOWN")
      }
    }
  }

  return (
    <div>
      <h1>Chauffeurs</h1>
      <div className='message'>
        {
          message && 
          <p 
          className={message ? (message.includes('bien ajouté') ? 'valid' : 'invalid') : ''}
          >
            {message} 
          </p>}
      </div>
      
        <form onSubmit={handleSubmit}>
          <div>
            <label>Code Permanent:</label>
            <input 
              type="text"
              placeholder='MB XXX'
              required
              name='codePermanent'
              onChange={handleChange}
              value={formData.codePermanent}
            />
            {
              errors.codePermanent && 
              <span 
                className={errors.codePermanent ? (errors.codePermanent.includes('disponible') ? 'valid' : 'invalid') : ''}
              >
                {errors.codePermanent
              }</span>}
          </div>
          <div>
            <label>Nom:</label>
            <input 
              type="text"
              placeholder="N'diaye"
              name='nom'
              required
              onChange={handleChange}
              value={formData.nom} 
            />
          </div>
          <div>
            <label>Prénom:</label>
            <input 
              type="text"
              placeholder='Abdoulaye'
              required
              name='prenom'
              onChange={handleChange}
              value={formData.prenom}
             />
          </div>
          <div>
            <label>Adresse:</label>
            <input 
              type="text"
              placeholder='Pikine, Tally Bou Mak'
              required
              name='adresse'
              onChange={handleChange}
              value={formData.adresse} 
            />
          </div>
          <div>
            <label>Téléphone:</label>
            <input 
              type="tel"
              placeholder='77 123s 45 67'
              required
              name='telephone'
              onChange={handleChange}
              value={formData.telephone} 
            />
          </div>
          <div>
            <label>Date de Naissance:</label>
            <input 
              type="date"
              name='dateNaissance'
              required
              onChange={handleChange}
              value={formData.dateNaissance} 
            />
          </div>
          <button type="submit">Soumettre</button>
        </form>
    </div>
  );
};

export default Chauffeurs;
