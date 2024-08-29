import React, { useState, useContext, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Context } from "../store/appContext";

export const Login = () => {
    const { actions } = useContext(Context);
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [welcomeMessage, setWelcomeMessage] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        
        const token = localStorage.getItem('token');
        if (token) {
            setWelcomeMessage('Welcome back to account!');
        } else {
            alert("Login failed, please check your credentials");
        }
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const success = await actions.login(name, email, password);
        if (success) {
            setWelcomeMessage('Welcome to the page!'); 
        } 
    };

    return (
        <div className="container d-flex justify-content-center align-items-center vh-100 bg-light">
            <div className="card p-4 shadow" style={{ maxWidth: '400px', width: '100%' }}>
                
                {welcomeMessage && <div className="alert alert-success text-center">{welcomeMessage}</div>}
                <button>Logout</button>
            </div>
        </div>
    );
};
