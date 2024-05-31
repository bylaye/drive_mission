import axios from 'axios';
import React, { useState, useEffect } from 'react';

const Acceuil = () =>{

    // const [message, setMessage] = useState('')

    const [missions, setMissions] = useState([]);
    const [chauffeurs, setChauffeurs] = useState([]);
    const [engins, setEngins] = useState('');

    useEffect(() => {
        const handleMission = async () => {
            try{
                const response = await axios.get(`http://localhost:8000/missions/get/all`);
                setMissions(response.data);
                console.log(response.data);                
            }catch (error){
                console.log('Error', error);
            }
        };
        handleMission();
    }, []);

    useEffect(() => {
        const handleChauffeur = async () => {
            try{
                const response = await axios.get(`http://localhost:8000/chauffeurs/get/all`);
                setChauffeurs(response.data);          
            }catch (error){
                console.log('Error', error);
            }
        };
        handleChauffeur();
    }, []);

    useEffect(() => {
        const handleEngin = async () => {
            try{
                const response = await axios.get(`http://localhost:8000/engins/get/all`);
                setEngins(response.data);         
            }catch (error){
                console.log('Error', error);
            }
        };
        handleEngin();
    }, []);
    

    return (
        <div className='acceuil1'>
            <div><p>Missions<br/> {missions.length}</p></div>
            <div><p>Chauffeurs<br/>  {chauffeurs.length}</p></div>
            <div><p>Engins <br/> {engins.length}</p></div>
        </div>
        
    )
    
}

export default Acceuil;