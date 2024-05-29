import axios from 'axios';
import React, { useState } from 'react';

const MissionEngins = () => {

    const [formData, setFormData] = useState({
        idMission: '',
        idEngin: '',
        codeMission: '',
    });

    const [message, setMessage] = useState('');
    const [missions, setMissions] = useState({})


    const handleChange = (e) =>{
        const {name, value} = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const checkMission = async () => {
        try{
            console.log('code mission', formData.codeMission)
            await axios.get(`http://localhost:8000/missions/get/codemission/${formData.codeMission}`);
            setMessage('Mission trouve');
            const r = await getMissionEnginRun();
            const formattedMissions = formatMissions(r.data);
            setMissions(formattedMissions);
            
        }catch (error){
            console.log(error.response.data);
            setMessage('Mission non trouve');
        }
    };


    const getMissionEnginRun = async () =>{
        try{
            const response = await axios.get(`http://localhost:8000/missions/get/mission/engin/run/all`);
            return response
        }catch (error){
            console.log(error);
        }
    };

    const formatMissions = (data) => {
        const formatted = {};
        data.forEach(mission => {
            const { immatricule, idEngin, codeMission } = mission;
            if (!formatted[immatricule]) {
                formatted[immatricule] = {
                    idEngin,
                    codeMissions: []
                };
            }
            if (codeMission) {
                formatted[immatricule].codeMissions.push(codeMission);
            }
        });
        return formatted;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        try{
            console.log(formData);

        }catch (error){
            console.log('error', error)
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
            <h1>Affecter Engin a la Mission</h1>
            <div className='message'>
                { message && 
                <p className={message ? (message.includes('non') ? 'invalid' : 'valid') : ''}>
                    {message} 
                </p> }
            </div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Code Mission</label>
                    <input
                        type='text'
                        name='codeMission'
                        value={formData.codeMission}
                        onChange={handleChange}
                    >
                    </input>
                    <button type='button' onClick={checkMission}>Get Mission</button>
                </div>
                <div>
                    <label>Engin Immatricule</label>
                    <input 
                        type='text'
                        name=''
                    >
                    </input>
                </div>
                <div>
                    {Object.keys(missions).length > 0 && (
                        <ul>
                            {Object.entries(missions).map(([immatricule, details]) => (
                                <li key={immatricule}>
                                    idEngin: {details.idEngin}: <strong>{immatricule}</strong>, codeMissions: {details.codeMissions.join(', ')} {details.codeMissions.length}
                                </li>
                            ))}
                        </ul>
                    )}
                </div>
                <button type='submit'>Soumettre</button>
            </form>
            
        </div>
    );

}

export default MissionEngins;