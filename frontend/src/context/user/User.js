import React, { useContext, useEffect, useState } from 'react'
import UserContext from './UserContext'
import { toast } from 'react-toastify';
import StateContext from '../state/StateContext';
import axios from 'axios';

const User = (props) => {

    const { setEmployees, setClient, FCM_token, setFCM_token, setAllTickets, setTickets } = useContext(StateContext)
    const [user, setUser] = useState('');
    const token = localStorage.getItem("token")

    const getUser = async () => {
        console.log(token);
        try {
            const response = await axios.get("http://127.0.0.1:8000/" + `api/get_user/?token=${token}`, {
                headers: {
                    'Content-Type': "application/json",
                }
            });

            const json = response.data;
            if (json.success) {
                setUser(json.user);
            } else {
                console.log(json.message);
                toast.error(json.error || json.message || "Some Error occurred");
            }
        } catch (error) {
            console.error(error);
        }
    };

    const [authenticated, setAuthenticated] = useState(false)
    const checkUserIsAuthenticated = async () => {
        if (!token) {
            return false;
        }
        const data = await fetch("http://127.0.0.1:8000/" + "api/token/verify/", {
            method: 'POST',
            body: JSON.stringify({ "token": token }),
            headers: { "Content-Type": "application/json", "token": `${token}`}
        })
        const result = await data.text();
        if (result) {
            setAuthenticated(true)
            return true;
        } else {
            setAuthenticated(false)
            return false
        }
    }

return (
    <UserContext.Provider value={{ user, setUser, getUser, checkUserIsAuthenticated, authenticated }}>
        {props.children}
    </UserContext.Provider>
)
}

export default User
