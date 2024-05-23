// src/Missions.js

import React, { useState } from 'react';

const Missions = () => {
  const [showForm, setShowForm] = useState(false);

  const handleAddClick = () => {
    setShowForm(true);
  };

  return (
    <div>
      <h1>Missions</h1>
      <button onClick={handleAddClick}>Ajouter une Mission</button>
      <button>Modifier une Mission</button>
      {showForm && (
        <form>
          <div>
            <label>Date de début:</label>
            <input type="date" />
          </div>
          <div>
            <label>Date de fin:</label>
            <input type="date" />
          </div>
          <div>
            <label>Chauffeur:</label>
            <input type="text" />
          </div>
          <div>
            <label>Engin:</label>
            <input type="number" />
          </div>
          <div>
            <label>Description:</label>
            <input type="text" />
          </div>
          <button type="submit">Soumettre</button>
        </form>
      )}
    </div>
  );
};

export default Missions;
