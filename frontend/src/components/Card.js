import React from 'react'
import styles from '../styles/card.module.css'

function Card({ data }) {


    return (
        <>
            <div className={styles.card}>
                <div className={styles.image}>
                    <img src="/images/book.webp" alt="" />
                </div>
                <div className={styles.data}>
                    <h3>{data.title}</h3>
                    <p>{data.author} - {data.year}</p>
                    <p>{data.description}</p>
                </div>
            </div>
        </>
    )
}

export default Card
