import React, { useContext, useEffect, useState } from 'react'
import styles from '../styles/register.module.css'
import axios from 'axios';
import StateContext from '../context/state/StateContext';
import { toast } from 'react-toastify';


const UpdateBook = () => {

    const [book, setBook] = useState({ isbn: '', title: '', description: "", author: '', publisher: '', year: '', genre: '', quantity: '' });
    const { setLoading, setBooks, books, updateBook, setUpdateBook } = useContext(StateContext);
    const [trending, setTrending] = useState(false);
    const [disabled, setDisabled] = useState(true);


    const handleChange = (e) => {
        setDisabled(false)
        const { name, value } = e.target;
        setBook(prevState => ({
            ...prevState,
            [name]: value
        }));
    }

    console.log(updateBook);

    useEffect(() => {
        if (books.length > 0) {
            const currentBook = books.find(item => item.isbn === updateBook.isbn);
            if (currentBook) {
                setBook({
                    title: currentBook.title,
                    description: currentBook.description,
                    author: currentBook.author,
                    publisher: currentBook.publisher,
                    year: currentBook.year,
                    genre: currentBook.genre,
                    quantity: currentBook.quantity
                });
                setTrending(currentBook.trending);
            } else {
                // Handle the case when the book is not found
                setBook({
                    title: '',
                    description: '',
                    author: '',
                    publisher: '',
                    year: '',
                    genre: '',
                    quantity: 0
                });
                setTrending(false);
            }
        }
    }, []);

    const handleSubmit = async (e) => {
        const token = localStorage.getItem("token")
        e.preventDefault();
        try {
            setLoading({ open: true, text: "Adding" })
            const response = await axios.put(
                "http://127.0.0.1:8000/" + `api/books/?token=${token}`,
                {
                    title: book.book_title,
                    description: book.description,
                    author: book.author,
                    publisher: book.publisher,
                    year: book.year,
                    genre: book.genre,
                    quantity: book.quantity,
                    trending: trending,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    }
                }
            );
            const json = response.data;
            if (json.success) {
                toast.success("Success fully Added")
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
            <form onSubmit={handleSubmit}>
                <div className={styles.title}>
                    <h1>Update Book</h1>
                </div>
                <div className={styles.forms}>
                    <div className="row g-0">
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Book title</span>
                                <input type="text" className='input' value={book.title} onChange={handleChange} name='book_title' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Description</span>
                                <input type="text" className='input' value={book.description} onChange={handleChange} name='description' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Author</span>
                                <input type="text" className='input' value={book.author} onChange={handleChange} name='author' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Publisher</span>
                                <input type="text" className='input' value={book.publisher} onChange={handleChange} name='publisher' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Year</span>
                                <input type="text" className='input' value={book.year} onChange={handleChange} name='year' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>genre</span>
                                <input type="text" className='input' value={book.genre} onChange={handleChange} name='genre' placeholder='' />
                            </div>
                        </div>
                        <div className="col-sm-6">
                            <div className={styles.input_field2}>
                                <span>Quantity</span>
                                <input type="number" className='input' value={book.quantity} onChange={handleChange} name='quantity' placeholder='' />
                            </div>
                        </div>
                        <div className={`form-check p-4 `}>
                            <input className="form-check-input" checked={trending} type="checkbox" onClick={() => setTrending(true)} value="" id="" />
                            <label className="form-check-label" for=""> Trending </label>
                        </div>
                    </div>

                    <div className="d-flex align-items-center justify-content-end">
                        <button type='button' className='button mt-0' onClick={() => setUpdateBook({ open: false, isbn: '' })}>Cancel</button> <button type="submit" disabled={disabled} class="button border mt-0">Add Book</button>
                    </div>
                </div>
            </form>
        </>
    )
}

export default UpdateBook
