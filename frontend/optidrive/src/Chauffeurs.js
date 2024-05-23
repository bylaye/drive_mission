// src/Chauffeurs.js

import React, { useState } from 'react';

const Chauffeurs = () => {
  const [showForm, setShowForm] = useState(false);

  const handleAddClick = () => {
    setShowForm(true);
  };

  return (
    <div>
      <h1>Chauffeurs</h1>
      <button onClick={handleAddClick}>Ajouter un Chauffeur</button>
      <button>Modifier un Chauffeur</button>
      {showForm && (
        <form>
          <div>
            <label>Nom:</label>
            <input type="text" />
          </div>
          <div>
            <label>Prénom:</label>
            <input type="text" />
          </div>
          <div>
            <label>Adresse:</label>
            <input type="text" />
          </div>
          <div>
            <label>Téléphone:</label>
            <input type="tel" />
          </div>
          <button type="submit">Soumettre</button>
        </form>
      )}
    </div>
  );
};

export default Chauffeurs;
