import React from 'react'
import styles from '../styles/checkout.module.css'

function Checkout() {
    return (
        <>
            <div className={`containerfluid ${styles.checkout}`}>
                <div className="container">
                    <h3>Checkout</h3>
                    <div className="row">
                        <div className="col-lg-8 col-md-6">
                            <div className={styles.customer}>
                                <div className={styles.head}>
                                    <h5>Customer Info</h5>
                                    <b>Required*</b>
                                </div>
                                <div className={styles.details}>
                                    <span>Full Name*</span>
                                    <input type="text" className='input' placeholder='' />
                                </div>
                                <div className={styles.details}>
                                    <span>Email*</span>
                                    <input type="text" className='input' placeholder='' />
                                </div>
                                <div className={styles.details}>
                                    <span>Phone no*</span>
                                    <input type="number" className='input' placeholder='' />
                                </div>
                            </div>

                            <div className={styles.customer}>
                                <div className={styles.head}>
                                    <h5>Address</h5>
                                    <b>Required*</b>
                                </div>
                                
                                <div className={styles.details}>
                                    <span>Street Address*</span>
                                    <input type="text" className='input' placeholder='' />
                                </div>
                                <div className={styles.details}>
                                    <div className="row">
                                        <div className="col-lg-4">
                                            <span>City*</span>
                                            <input type="text" className='input' placeholder='' />
                                        </div>
                                        <div className="col-lg-4">
                                            <span>State*</span>
                                            <input type="text" className='input' placeholder='' />
                                        </div>
                                        <div className="col-lg-4">
                                            <span>Pincode*</span>
                                            <input type="text" className='input' placeholder='' />
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div className={styles.customer}>
                                <div className={styles.head}>
                                    <h5>Book Issue</h5>
                                    <b>Required*</b>
                                </div>

                                <div className={styles.details}>
                                    <div className="row">
                                        <div className="col-lg-6">
                                            <span>From *</span>
                                            <input type="date" className='input' placeholder='' />
                                        </div>
                                        <div className="col-lg-6">
                                            <span>to *</span>
                                            <input type="date" className='input' placeholder='' />
                                        </div>
                                        <div className={styles.details}>
                                            <span>Quantiy*</span>
                                            <input type="number" className='input' placeholder='' />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div className="col-lg-4 col-md-6">
                        <div className={styles.customer}>
                                <div className={styles.head}>
                                    <h5>Books</h5>
                                    <b>Required*</b>
                                </div>
                                <div className={styles.order}>
                                    <div className={styles.data}>
                                        <div className={styles.item}>
                                            <img src={process.env.REACT_APP_API_URL + `media/product_images/bed1.png`} alt="" />
                                        </div>
                                        <div className={styles.quntity}>
                                            <p>Book1</p>
                                            <p>Quantity : 1</p>
                                        </div>
                                    </div>
                                    <div className={styles.amount}>
                                        <p>&#8377;200.00</p>
                                    </div>
                                </div>
                            </div>
                            <div>
                                <a href="" className="button">Checkout</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Checkout
