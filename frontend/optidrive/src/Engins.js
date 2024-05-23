// src/Engins.js

import React, { useState } from 'react';

function Engins({ action }) {
  const [formData, setFormData] = useState({
    idChauffeur: '',
    capacite: '',
    isRemorque: false,
    immatricule: '',
    marque: '',
    typeEngin: '',
    annee: '',
    typeFuel: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleRadioChange = (e) => {
    const { value } = e.target;
    setFormData((prev) => ({ ...prev, isRemorque: value === 'oui' }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Here you can handle the form submission, for example, by sending the data to your backend
    console.log('Form data submitted:', formData);
  };

  return (
    <div>
      <h2>{action === 'add' ? 'Ajouter un Engin' : 'Modifier un Engin'}</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>ID Chauffeur</label>
          <input
            type="number"
            name="idChauffeur"
            value={formData.idChauffeur}
            onChange={handleChange}
          />
        </div>

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
          <label>Remorque</label>
          <div>
            <label>
              <input
                type="radio"
                name="isRemorque"
                value="oui"
                checked={formData.isRemorque === true}
                onChange={handleRadioChange}
              />
              Oui
            </label>
            <label>
              <input
                type="radio"
                name="isRemorque"
                value="non"
                checked={formData.isRemorque === false}
                onChange={handleRadioChange}
              />
              Non
            </label>
          </div>
        </div>
        
        <div>
          <label>Type d'Engin</label>
          <select
            name="typeEngin"
            value={formData.marque}
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
          <label>Année</label>
          <input
            type="number"
            name="annee"
            value={formData.annee}
            onChange={handleChange}
          />
        </div>
        <div>
          <label>Type de Fuel</label>
          <input
            type="text"
            name="typeFuel"
            value={formData.typeFuel}
            onChange={handleChange}
          />
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
