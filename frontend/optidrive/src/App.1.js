import React, { useState } from 'react';
import Engins from './Engins';
import Chauffeurs from './Chauffeurs';
import Missions from './Missions';
import EnginChauffeur from './EnginChauffeur';
import MissionEngins from './MissionEngins';
import Partenaires from './Partenaires';
import Acceuil from './Acceuil';

export function App() {
  const [activeTab, setActiveTab] = useState('acceuil');
  // const [openMenu, setOpenMenu] = useState({
  //   chauffeurs: false,
  //   missions: false,
  //   engins: false,
  // });
  const [openMenu, setOpenMenu] = useState('engins')

  const handleMenuClick = (menu) => {
    setOpenMenu(openMenu === menu ? '' : menu);
    // setOpenMenu((prev) => ({ ...prev, [menu]: !prev[menu] }));
  };
  return (
    <div className="App">
      <div className='sidebar'>

        {<button onClick={() => setActiveTab('acceuil')}>Acceuil</button>}
        
        {<button onClick={() => setActiveTab('addPartenaire')}>Partenaires</button>}
        
        <button onClick={() => handleMenuClick('chauffeurs')}>Chauffeurs </button>
        {openMenu === "chauffeurs" && (
          <div className="submenu">
            <button onClick={() => setActiveTab('addChauffeur')}>Ajouter un Chauffeur</button>
            <button onClick={() => setActiveTab('listChauffeur')}>Liste des Chauffeurs</button>
          </div>
        )}

        <button onClick={() => handleMenuClick('engins')}>Engins</button>
        {openMenu === 'engins' && (
          <div className="submenu">
            <button onClick={() => setActiveTab('addEngin')}>Ajouter Engin</button>
            <button onClick={() => setActiveTab('assignEnginChauffeur')}>Assigner Chauffeur</button>
          </div>
        )}

        <button onClick={() => handleMenuClick('missions')}>Missions</button>
        {openMenu === 'missions' && (
          <div className="submenu">
            <button onClick={() => setActiveTab('addMission')}>Ajouter Mission</button>
            <button onClick={() => setActiveTab('affecterMission')}>Affecter Engin</button>
          </div>
        )}

        
      </div>

      <div className="content">
        {activeTab === 'addEngin' && <Engins action="addEngin" />}
        {activeTab === 'assignEnginChauffeur' && <EnginChauffeur />}
        {activeTab === 'addMission' && <Missions action="addMission" />}
        {activeTab === 'affecterMission' && <MissionEngins  />}
        {activeTab === 'addPartenaire' && <Partenaires  />}
        {activeTab === 'acceuil' && <Acceuil />}
        {activeTab === 'addChauffeur' && <Chauffeurs action="addChauffeur" />}
        {activeTab === 'enginChauffeur' && <Chauffeurs action="enginChauffeur" />}
      </div>
    </div>
  );
}
