import React, { useContext, useEffect, useState } from 'react'
import UserContext from './UserContext'
import { toast } from 'react-toastify';
import StateContext from '../state/StateContext';
import axios from 'axios';

const User = (props) => {

    const { setBooks } = useContext(StateContext)
    const [user, setUser] = useState('');
    const token = localStorage.getItem("token")


    const getUser = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/" + `api/getUser/?token=${token}`, {
                headers: {
                    'Content-Type': "application/json",
                }
            });

            const json = response.data;
            console.log(json);
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
            headers: { "Content-Type": "application/json", "token": `${token}` }
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

    const getBooks = async () => {
        try {
            const response = await axios.get("http://127.0.0.1:8000/" + `api/books/?token=${token}`, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            const json = response.data;
            console.log(json);
            if (json.success) {
                const sorted = json.book.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
                setBooks(sorted);
            } else {
                toast.error(json.error || json.message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <UserContext.Provider value={{ user, setUser, getUser, checkUserIsAuthenticated, authenticated, getBooks }}>
            {props.children}
        </UserContext.Provider>
    )
}

export default User
