import React from 'react'
import styles from '../styles/register.module.css'

function Addbook() {
  return (
    <>
       <div className="container mt-5">
                <div className={styles.formContainer}>
                    <form action="">
                        <div className="row">
                            <div className="col-12">
                                <div className={styles.title}>
                                    <h1>Add Book</h1>
                                </div>
                                <div className={styles.forms}>
                                    <div className={styles.input_field2}>
                                        <span>Book Name</span>
                                        <input type="text" className='input' name='book_name' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Description</span>
                                        <input type="text" className='input' name='description' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Author</span>
                                        <input type="text" className='input' name='author' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Publisher</span>
                                        <input type="text" className='input' name='author' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Year</span>
                                        <input type="text" className='input' name='author' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>gener</span>
                                        <input type="text" className='input' name='author' placeholder='' />
                                    </div>
                                    <div className={styles.input_field2}>
                                        <span>Quantity</span>
                                        <input type="number" className='input' name='author' placeholder='' />
                                    </div>
                                    <div className={`form-check p-4 `}>
                                        <input className="form-check-input" type="checkbox" value="" id="" />
                                        <label className="form-check-label" for=""> Trending </label>
                                    </div>
                                        
                                    <div className={styles.button1}>
                                        <button type="submit" class="button border">Add Book</button>
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

export default Addbook
