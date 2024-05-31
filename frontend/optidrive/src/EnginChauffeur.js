import React, { useState } from 'react';
import axios from 'axios';

function EnginChauffeur(){
    const [immatriculeQuery, setImmatriculeQuery] = useState('');
  const [chauffeurQuery, setChauffeurQuery] = useState('');
  const [ , setChauffeurId] = useState(null);
  const [ , setEnginImmatricule] = useState(null);
  const [idEnginImmatricule, setIdEnginImmatricule] = useState(null);
  const [message, setMessage] = useState('');

  const checkEnginChauffeur = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/engins/get/immatricule/${immatriculeQuery}`);
      console.log('Reponse ', response)
      setChauffeurId(response.data.idChauffeur);
      setIdEnginImmatricule(response.data.idEngin)
      setMessage(`Chauffeur actuel ID: ${response.data.idChauffeur || 'Aucun chauffeur assigné'}`);
    } catch (error) {
        if (error.response && error.response.data && error.response.data.detail) {
            setMessage(`Erreur : ${error.response.data.detail}`);
        } else {
            setMessage('UNKNOWN ERROR');
        }
    }
  };

  const unassignEnginChauffeur = async () => {
    try{
        const response = await axios.put(`http://localhost:8000/engins/update/engin/unassign/${immatriculeQuery}`, 
            { headers: { 'Content-Type': 'application/json',},
        });
        console.log('Engin ID ', idEnginImmatricule, response.data)
        setMessage(`Engin ${response.data.immatricule} n'est plus assigne`);

    } catch (error) {
        if (error.message === 'Network Error') {
          setMessage('Erreur réseau : Impossible de se connecter');
        }
        else if (error.response && error.response.data && error.response.data.detail) {
            setMessage(`Erreur : ${error.response.data.detail}`);
        } else {
            setMessage('UNKNOWN Erreur lors de la désassignation du chauffeur');
        }
        throw error; 
    }
  };

  const checkChauffeurEngin = async () => {
    try {
      const responseGetChauffeur = await axios.get(`http://localhost:8000/chauffeurs/get/chauffeurs/codepermanent/${chauffeurQuery}`);
      setChauffeurId(responseGetChauffeur.data.idChauffeur)
      const response = await axios.get(`http://localhost:8000/engins/get/chauffeur/codepermanent/${chauffeurQuery}`);
      setEnginImmatricule(response.data.immatricule);
      setMessage(`Engin actuel Immatricule: ${response.data.immatricule}`);
    } catch (error) {
        if (error.response && error.response.data && error.response.data.detail) {
            setMessage(`Erreur : ${error.response.data.detail}`);
        } else {
            setMessage('UNKNOWN ERROR');
        }  
    }
  };


  const unassignChauffeurEngin = async () => {
    try{
        const response = await axios.put(`http://localhost:8000/engins/update/engin/unassign/chauffeur/${chauffeurQuery}`);
        setMessage(`Chauffeur Code Permanent ${chauffeurQuery} unassign engin immatricule ${response.data.immatricule}`);
    } catch (error) {
        if (error.message === 'Network Error') {
          setMessage('Erreur réseau : Impossible de se connecter');
          throw error;
        }
        else if (error.response && error.response.data && error.response.data.detail) {
            setMessage(`Erreur : ${error.response.data.detail}`);
        } else {
            setMessage('UNKNOWN ERROR');
            throw error;
        } 
        // throw error; // propager l'erreur sur une fonction qui l'appel
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        await unassignEnginChauffeur();
        await unassignChauffeurEngin();
        const response = await axios.put(`http://localhost:8000/engins/update/engin/chauffeur/${immatriculeQuery}`, {
        codePermanent: chauffeurQuery
        }, {
        headers: {
            'Content-Type': 'application/json',
        },
        });
        
        setMessage(`${response.data.prenom} ${response.data.nom} assigné avec succès engin ${response.data.immatricule}`);
    } catch (error) {
      console.error('Erreur lors de la mise à jour du chauffeur', error);
      if (error.response && error.response.data && error.response.data.detail) {
        setMessage(`Erreur : ${error.response.data.detail}`);
      } else {
        setMessage('Erreur lors de la mise à jour du chauffeur');
      }
    }
  };

    return (
        <div>
            <h2>Assigner Engin à un Chauffeur</h2>
            {message && <p>{message}</p>}
            <form class="updates" onSubmit={handleSubmit}>
            <div>
                <label>Immatricule Engin</label>
                <input
                type="text"
                value={immatriculeQuery}
                onChange={(e) => setImmatriculeQuery(e.target.value)}
                />
                <button type="button" onClick={checkEnginChauffeur}>Vérifier Engin</button>
                <button class='unassign' type="button" onClick={unassignEnginChauffeur}>Unassign Engin</button>
            </div>
            <div>
                <label>Code Permanent Chauffeur</label>
                <input
                type="text"
                value={chauffeurQuery}
                onChange={(e) => setChauffeurQuery(e.target.value)}
                />
                <button type="button" onClick={checkChauffeurEngin}>Vérifier Chauffeur</button>
                <button class='unassign' type="button" onClick={unassignChauffeurEngin}>Unassign Chauffeur</button>
            </div>
            <button type="submit">Assigner</button>
            </form>
        </div>
        );
}

export default EnginChauffeur;