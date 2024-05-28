import axios from 'axios';
import React, { useState } from 'react';

const MissionEngins = () => {

    const [formData, setFormData] = useState({
        idMission: '',
        idEngin: '',
        codeMission: '',
    });

    const [message, setMessage] = useState('');


    const handleChange = (e) =>{
        const {name, value} = e.target;
        setFormData((prev) => ({ ...prev, [name]: value }));
    };

    const checkMission = async () => {
        try{
            console.log('code mission', formData.codeMission)
            const response = await axios.get(`http://localhost:8000/missions/get/codemission/${formData.codeMission}`);
            setMessage('Mission trouve');
            const r = await getMissionEnginRun();
            console.log(r.data)
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
    }

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
            <form>
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
                <button type='submit'>Soumettre</button>
            </form>
        </div>
    );

}

export default MissionEngins;