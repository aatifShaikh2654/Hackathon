import React, { useContext, useEffect, useState } from 'react'
import UserContext from './UserContext'
import { toast } from 'react-toastify';
import StateContext from '../state/StateContext';
import axios from 'axios';

const User = (props) => {

    const { setBooks } = useContext(StateContext)
    const [user, setUser] = useState('');
    const token = localStorage.getItem("token")
    const [trending, setTrending] = useState([]);
    const [arrival, setArrival] = useState([]);
    const [otherBooks, setOtherBooks] = useState([]);
    

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
        const token = localStorage.getItem('token')
        if (!token) {
            return false;
        }
        const data = await axios.post("http://127.0.0.1:8000/" + "api/token/verify/", { token: token }, {
            headers: { "Content-Type": "application/json" }
        })
        const result = data.data;
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
            if (json.success) {
                const sorted = json.book.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
                setBooks(sorted);
                const trending = sorted.filter(item => item.trending);
                setTrending(trending);
                const arrival = sorted.filter(item => item.new_arrival);
                setArrival(arrival);
                const otherBooks = sorted.filter(item => !item.trending && !item.arrival);
                setOtherBooks(otherBooks);
            } else {
                toast.error(json.error || json.message);
            }
        } catch (error) {
            console.log(error);
        }
    };

    return (
        <UserContext.Provider value={{ user, trending, otherBooks, arrival, setUser, getUser, checkUserIsAuthenticated, authenticated, getBooks }}>
            {props.children}
        </UserContext.Provider>
    )
}

export default User
