import React from 'react'
import styles from '../styles/card.module.css'

function Card() {
    return (
        <>
            <div className={styles.card}>
                <div className={styles.image}>
                    <img src="/images/book.webp" alt="" />
                </div>
                <div className={styles.data}>
                    <h3>Book Name</h3>
                    <p>Author - 2017 </p>
                    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Ratione voluptatibus dolore sunt veritatis facilis quod ea accusamus, cum, fugiat sapiente suscipit illo incidunt fuga excepturi ab provident reiciendis enim odio.</p>
                </div>
            </div>
        </>
    )
}

export default Card
