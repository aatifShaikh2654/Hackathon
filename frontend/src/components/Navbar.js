import React, { useContext, useEffect } from 'react'
import styles from '../styles/navbar.module.css'
import { Link } from 'react-router-dom'
import UserContext from '../context/user/UserContext'

const Navbar = () => {

    const { checkUserIsAuthenticated, getUser, user } = useContext(UserContext)
    const token = localStorage.getItem("token")

    useEffect(() => {
        if (token) {
            getUser();
        }
        console.log(user);
    }, [])

  return (
    <>
        <header className='container'>
            <nav className={styles.navbar}>
                <Link to="/" className={styles.logo}>
                    <img src="/images/book.webp" className='img-fluid' alt="" />
                    <h2>Public Library</h2>
                </Link>
                <div className={styles.links}>
                    <Link className='button' to="/login">Login</Link>
                </div>
            </nav>
        </header>
    </>
  )
}

export default Navbar
