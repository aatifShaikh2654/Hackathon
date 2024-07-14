import React, { useContext } from 'react'
import styles from '../styles/card.module.css'
import StateContext from '../context/state/StateContext'
import axios from 'axios'
import { toast } from 'react-toastify'
import { Link } from 'react-router-dom'

function Card({ data, setUpdate, profile }) {

    const { setUpdateBook, setLoading, setBooks } = useContext(StateContext)

    const handleSubmit = async (e) => {
        const token = localStorage.getItem("token")
        e.preventDefault();
        try {
            setLoading({ open: true, text: "Adding" })
            const response = await axios.delete(
                "http://127.0.0.1:8000/" + `api/books/?token=${token}`,
                {
                    isbn: data.isbn
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }
            );
            const json = response.data;
            if (json.success) {
                toast.success("Success fully deleted")
                setBooks(prevbooks => [...prevbooks, json.book])
                setUpdateBook({ open: false, isbn: '' })
            } else {
                toast.error(json.error || json.message)
            }

        } catch (error) {
            console.log(error);
            toast.error(error)
        } finally {
            setLoading({ open: false, text: '' })
        }
    }

    return (
        <>
            <div className={styles.card}>
                <div className={styles.image}>
                    <img src="http://books.google.com/books/content?id=yDB0tAEACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api" alt="" />
                </div>
                <div className={styles.data}>
                    <h3>{data.title}</h3>
                    <p>{data.author} - {data.year}</p>
                    <p>{data.description}</p>
                    <p>Genre - {data.genre}</p>
                    <div className="d-flex align-items-center">
                        <Link to='/checkout' onClick={handleSubmit} className='button mt-0 me-0' style={{ fontSize: "1rem", padding: "5px 20px" }}>Checkout</Link>
                        {profile ?
                            <div>
                                <button onClick={() => { setUpdateBook({ open: true, isbn: data.isbn }) }} className='button border mb-3 me-0' style={{ fontSize: "1rem", padding: "5px 20px" }}> update</button>
                                <button onClick={handleSubmit} className='button mb-3 me-0' style={{ fontSize: "1rem", padding: "5px 20px" }}>Delete</button>
                            </div>
                            : null}
                    </div>
                </div>
            </div>
        </>
    )
}

export default Card
