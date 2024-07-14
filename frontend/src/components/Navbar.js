import React from 'react'
import styles from '../styles/navbar.module.css'

const Navbar = () => {
  return (
    <>
        <header className='container'>
            <nav className={styles.navbar}>
                <div className={styles.logo}>
                    <img src="/images/book.webp" className='img-fluid' alt="" />
                    <h2>Public Library</h2>
                </div>
                <div className={styles.links}>
                    <button className='button'>Login</button>
                </div>
            </nav>
        </header>
    </>
  )
}

export default Navbar
