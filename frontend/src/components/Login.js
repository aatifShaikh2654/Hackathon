import React, { useContext, useState } from 'react'
import styles from '../styles/register.module.css'
import { Link, useNavigate } from 'react-router-dom'
import StateContext from '../context/state/StateContext'
import axios from 'axios'
import { toast } from 'react-toastify'
import UserContext from '../context/user/UserContext'


const Login = () => {

    const { setLoading } = useContext(StateContext);
    const { setUser } = useContext(UserContext)
    const [formData, setFormData] = useState({ email: "", password: "" });
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setError('')
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            setLoading({ open: true, text: 'Verifying...' })
            const response = await axios.post("http://127.0.0.1:8000/" + "api/login/", formData, {
                headers: {
                    'Content-type': "application/json"
                },
            })

            const json = response.data;
            console.log(json)
            if (json.success) {
                if (json.user.verified == true) {
                    toast.success("Successfully Logged in")
                    setUser(json.user)
                    localStorage.setItem("token", json.access)
                    navigate('/')
                } else {
                    toast.error("You are not Verified")
                }
            } else {
                console.log(json);
                setError(json.message || json.message[0].msg)
                console.log(json.error);
            }


        } catch (error) {
            console.log(error);
            setError(error.response.data.message || error.response.data.message[0].msg)
            console.log("Some Thing Went wrong");
        } finally {
            setLoading({ open: false, text: '' })
        }
    }



    return (
        <>
            <div className="container mt-5">
                <div className={styles.formContainer}>
                    <form action="" onSubmit={handleSubmit}>
                        <div className="row">
                            <div className="col-12">
                                <div className={styles.title}>
                                    <h1>Login</h1>
                                </div>
                                <div className={styles.forms}>
                                    <div className={styles.input_field2}>
                                        <span>Email</span>
                                        <input type="email" className='input' onChange={handleChange} name='email' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Password</span>
                                        <input type="password" className='input' onChange={handleChange} name='password' placeholder='' />
                                    </div>
                                    <div className={styles.button1}>
                                        <button type="submit" class="button border">Login</button>
                                    </div>
                                    {error ? <p style={{color: "red", padding: "0px 10px"}}>{error}</p> : null}
                                    <div className={styles.google}>
                                        <Link to="/register">Don't have an account, Register</Link>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </>
    )
}

export default Login
