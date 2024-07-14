import React, { useContext, useEffect } from 'react'
import styles from '../styles/navbar.module.css'
import { Link, useNavigate } from 'react-router-dom'
import UserContext from '../context/user/UserContext'

const Navbar = () => {

    const { checkUserIsAuthenticated, getUser, user } = useContext(UserContext)
    const token = localStorage.getItem("token")
    const navigate = useNavigate();

    useEffect(() => {
        if (token) {
            getUser();
        }
    }, [])

    const handleLogout = () => {
        localStorage.removeItem("token")
        navigate('/')
    }

  return (
    <>
        <header className='container'>
            <nav className={styles.navbar}>
                <Link to="/" className={styles.logo}>
                    <img src="/images/book.webp" className='img-fluid' alt="" />
                    <h2>Public Library</h2>
                </Link>
                <div className={styles.links}>
                    {user.verified ? <Link className='button border' to="/profile">Profile</Link> : null}
                    {token ? <Link className='button border ms-2' onClick={handleLogout}>Logout</Link> : <Link className='button' to="/login">Login</Link>}
                </div>
            </nav>
        </header>
    </>
  )
}

export default Navbar
