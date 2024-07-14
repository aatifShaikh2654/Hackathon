import React from 'react'
import styles from '../styles/navbar.module.css'
import { Link } from 'react-router-dom'

const Navbar = () => {
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
