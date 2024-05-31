// src/Engins.js

import React, { useState } from 'react';
import axios from 'axios';

function Engins({ action }) {
  const [formData, setFormData] = useState({
    idChauffeur: null,
    capacite: 0,
    is_remorque: false,
    immatricule: '',
    marque: '',
    typeEngin: '',
    annee: '',
    typeFuel: '',
  });

  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  // const handleRadioChange = (e) => {
  //   const { value } = e.target;
  //   setFormData((prev) => ({ ...prev, is_remorque: value === 'oui' }));
  // };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Here you can handle the form submission, for example, by sending the data to your backend
    console.log('Form data submitted:', formData);
    try{
      const response = await axios.post('http://localhost:8000/engins/add',{
        ...formData,
        idChauffeur: formData.idChauffeur ? parseInt(formData.idChauffeur) : null,
      }, {
        headers:{'Content-Type': 'application/json',},
      });

      if (response.status === 200){
        setMessage(`Engin ${response.data.immatricule} Ajoute avec succes`)
        console.log("Engin Ajoute avec succes", response.request.response);
        // console.log('Response Request:', response.data);
      }
    } catch (error) {
      if (error.response){
        setMessage(`Engin, ${error.response.data.detail}`)
        console.log('W WWWW WWDDD',error.response.request.response, error.response.status, "QQQQ aaa")
      }
      // console.error('Error Data submitted', error)
    }
  };

  return (
    <div>
      <h2>{action === 'addEngin' ? 'Ajouter un Engin' : 'Modifier un Engin'} </h2>
      {message && <p>{message}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Immatricule</label>
          <input
            type="text"
            name="immatricule"
            value={formData.immatricule}
            onChange={handleChange}
          />
        </div>

        <div>
          <label>Capacité</label>
          <input
            type="number"
            name="capacite"
            value={formData.capacite}
            onChange={handleChange}
          />
        </div>
        
        <div>
          <label>Année</label>
          <input
            type="number"
            name="annee"
            value={formData.annee}
            onChange={handleChange}
          />
        </div>
        
        {/* <div>
          <label>Remorque</label>
          <div>
            <label>
              <input
                type="radio"
                name="is_remorque"
                value="oui"
                checked={formData.is_remorque === true}
                onChange={handleRadioChange}
              />
              Oui
            </label>
            <label>
              <input
                type="radio"
                name="is_remorque"
                value="non"
                checked={formData.is_remorque === false}
                onChange={handleRadioChange}
              />
              Non
            </label>
          </div>
        </div> */}
        
        <div>
          <label>Type d'Engin</label>
          <select
            name="typeEngin"
            value={formData.typeEngin}
            onChange={handleChange}
          >
            <option value="">Sélectionnez une marque</option>
            <option value="C1">C1</option>
            <option value="Caterpillar">Caterpillar</option>
            <option value="Poclain">Poclain</option>
          </select>
        </div>

        <div>
          <label>Marque</label>  
          <select
            name="marque"
            value={formData.marque}
            onChange={handleChange}
          >
            <option value="">Sélectionnez une marque</option>
            <option value="FIAT">FIAT</option>
            <option value="VOLVO">VOLVO</option>
            <option value="Renault">Renault</option>
            <option value="NISSAN">NISSAN</option>
          </select>
        </div>
        
        <div>
          <label>Type de Fuel</label>
          <select
            name="typeFuel"
            value={formData.typeFuel}
            onChange={handleChange}
          >
            <option value="">Sélectionnez une marque</option>
            <option value="GASOIL">GASOIL</option>
            <option value="ESSENCE">ESSENCE</option>
            <option value="ELECTRIQUE">ELECTRIQUE</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Engins;
