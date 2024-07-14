import React from 'react'
import styles from '../styles/dashboard.module.css'


const Dashboard = () => {
  return (
    <>
      <div className={styles.dashboard}>
          <div className={styles.search}>
            <h1>Search the books available in Library</h1>
            <div className={styles.searchbox}>
              <input type="text" />
              <button className='button'>search</button>
            </div>
          </div>
      </div>
    </>
  )
}

export default Dashboard
