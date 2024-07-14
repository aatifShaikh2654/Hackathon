import React, { useContext } from 'react'
import styles from '../styles/profile.module.css'
import Card from '../components/Card'
import UserContext from '../context/user/UserContext'

function Profile() {

    const { user } = useContext(UserContext);


    return (
        <>
            <div className="container">
                <div className={styles.profile}>
                    <div className="row">
                        <div className="col-lg-8">
                            <div className={styles.books}>
                                <h1>Search Book</h1>
                                <div className={styles.search}>
                                    <div className={styles.searchbox}>
                                        <input type="text" placeholder="Oddo Developement" />
                                        <button className='button'>search</button>
                                    </div>
                                </div>
                            </div>
                            <div className={styles.mybooks}>
                                <h1>My Books</h1>
                                <Card />
                                <div className={styles.status}>
                                    <button className='button'>3 Days Remains</button>
                                </div>
                            </div>
                        </div>
                        <div className="col-lg-4">
                            <div className={styles.user}>
                                <h1>User Profile</h1>
                                <div className={styles.name}>
                                    <div className="image">
                                        <img src="images/book.webp" alt="" />
                                    </div>
                                    <div>
                                        <h3 className={styles.prof}>{user.full_name}</h3>
                                        <p className={styles.prof}>{user.role == "User" ? '' : user.role}</p>
                                    </div>
                                </div>
                                <div className={styles.location}>
                                    <i class="fa-solid fa-location-dot"></i>
                                    <p>389,Shahpur,Ahmedabad-380001</p>
                                </div>
                                <div className={styles.location}>
                                    <i class="fa-solid fa-phone"></i>
                                    <p>+91 {user.phone}</p>
                                </div>
                                <div className={styles.location}>
                                    <i class="fa-solid fa-envelope"></i>
                                    <p>{user.email}</p>
                                </div>
                                <div className={styles.edit}>
                                    <a href="#"><i class="fa-solid fa-pen"></i> Edit Information</a>
                                </div>
                            </div>
                            <hr />
                            <h1>Your Contact</h1>
                            <hr />
                            <h3>Aatif Admin</h3>
                            <div className={styles.location}>
                                    <i class="fa-solid fa-location-dot"></i>
                                    <p>389,Shahpur,Ahmedabad-380001</p>
                                </div>
                                <div className={styles.location}>
                                    <i class="fa-solid fa-phone"></i>
                                    <p>+91 98522 XXXXX</p>
                                </div>
                                <div className={styles.location}>
                                    <i class="fa-solid fa-envelope"></i>
                                    <p>admin@gmail.com</p>
                                </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default Profile
