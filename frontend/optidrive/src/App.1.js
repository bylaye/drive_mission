import React, { useState } from 'react';
import Engins from './Engins';
import Chauffeurs from './Chauffeurs';
import Missions from './Missions';
import EnginChauffeur from './EnginChauffeur';

export function App() {
  const [activeTab, setActiveTab] = useState('engins');
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

        <button onClick={() => handleMenuClick('chauffeurs')}>Chauffeurs </button>
        {openMenu === "chauffeurs" && (
          <div className="submenu">
            <button onClick={() => setActiveTab('addChauffeur')}>Ajouter un Chauffeur</button>
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

        {/* <button onClick={() => setActiveTab('chauffeurs')}>Chauffeurs</button> */}
      </div>

      <div className="content">
        {activeTab === 'addEngin' && <Engins action="addEngin" />}
        {activeTab === 'assignEnginChauffeur' && <EnginChauffeur />}
        {activeTab === 'addMission' && <Missions action="addMission" />}
        {activeTab === 'affecterMission' && <Missions action="affecterMission" />}
        {activeTab === 'addChauffeur' && <Chauffeurs action="addChauffeur" />}
        {activeTab === 'enginChauffeur' && <Chauffeurs action="enginChauffeur" />}
      </div>
    </div>
  );
}
