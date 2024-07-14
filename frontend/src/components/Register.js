import React, { useContext, useState } from 'react'
import styles from '../styles/register.module.css'
import { useNavigate } from 'react-router-dom';
import axios from 'axios'
import { toast } from 'react-toastify';
import StateContext from '../context/state/StateContext';

const Register = () => {

    const { setLoading } = useContext(StateContext);
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
            setLoading({ open: true, text: 'Creating...' })
            const response = await axios.post("http://127.0.0.1:8000/" + "api/signup/",
                { role: select, full_name: formData.full_name, email: formData.email, password: formData.password },
                {
                    headers: {
                        'Content-type': "application/json"
                    },
                })

            const json = response.data;
            console.log(json);
            if (json.success) {
                console.log("Successfully Created");
                navigate('/')
                toast.success(json.success)
                if (json.access) {
                    localStorage.setItem("token", json.access)
                }
            } else {
                console.log(json.error);
                setError(json.message || json.message[0].msg)
                console.log("Some error Occurred");
            }


        } catch (error) {
            console.log(error);
            setError(error.response.data.message || error.response.data.message[0].msg)
            console.log("Some Thing Went wrong");
        } finally{
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
                                    {error ? <p style={{color: "red", padding: "0px 10px"}}>{error}</p> : null}
                                    <div className={styles.button1}>
                                        <button type="submit" class="button border">Register</button>
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
