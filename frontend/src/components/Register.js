import React, { useState } from 'react'
import styles from '../styles/register.module.css'
import { useNavigate } from 'react-router-dom';
import axios from 'axios'
import { toast } from 'react-toastify';

const Register = () => {

    const [formData, setFormData] = useState({ full_name: "", email: "", password: "" });
    const [drop, setDrop] = useState(false);
    const [error, setError] = useState('');
    const [select, setSelect] = useState('');

    const navigate = useNavigate();

    const selectDrop = (select) => {
        setSelect(select)
        setDrop(false)
    }


    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(process.env.REACT_APP_API_URL + "api/auth/createUser",
                { role: select, name: formData.name, email: formData.email, password: formData.password },
                {
                    headers: {
                        'Content-type': "application/json"
                    },
                })

            const json = response.data;
            console.log(json);
            if (json.success) {
                console.log("Successfully Created");
                toast.success('Successfully Logged in')
            } else {
                console.log(json.error);
                setError(json.message || json.message[0].msg)
                console.log("Some error Occurred");
            }


        } catch (error) {
            console.log(error);
            setError(error.response.data.message || error.response.data.message[0].msg)
            console.log("Some Thing Went wrong");
        }
    }



    return (
        <>
            <div className="container mt-5">
                <div className={styles.formContainer}>
                    <form action="">
                        <div className="row">
                            <div className="col-12">
                                <div className={styles.title}>
                                    <h1>Regestration</h1>
                                </div>
                                <div className={styles.forms}>
                                    <div className={styles.input_field2}>
                                        <span>Select Role</span>
                                        <div className={` ${styles.dropdown} ${drop ? styles.active : ''}`} onClick={() => setDrop(!drop)}>
                                            <div className={styles.select}>
                                                <div className="d-flex align-items-center">
                                                    <i className='bx bx-user-circle'></i>
                                                    <span>{select ? select : "Select Role"}</span>
                                                </div>
                                                <i className="fa-solid fa-angle-up"></i></div>
                                            <ul>
                                                <li onClick={() => { selectDrop('User') }}>User</li>
                                                <li onClick={() => { selectDrop('Librarian') }}>Librarian</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Full Name</span>
                                        <input type="text" className='input' onChange={handleChange} name='full_name' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Email</span>
                                        <input type="email" className='input' onChange={handleChange} name='email' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Password</span>
                                        <input type="password" className='input' onChange={handleChange} name='password' placeholder='' />
                                    </div>
                                    <div className={styles.button1}>
                                        <button type="button" class="button border">Register</button>
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

export default Register
