import React, { useContext, useEffect, useState } from 'react'
import styles from '../styles/dashboard.module.css';
import Card from '../components/Card';
import StateContext from '../context/state/StateContext';
import UserContext from '../context/user/UserContext';

const Dashboard = () => {

    const [searchResults, setSearchResults] = useState('');
    const { books } = useContext(StateContext);
    const { getBooks } = useContext(UserContext)

    const handleSearchInputChange = (event) => {
        const query = event.target.value;
        // Perform search/filtering logic
        const filteredResults = books.filter(book =>
            book.title.toLowerCase().includes(query.toLowerCase())
        );
        setSearchResults(filteredResults);
    };

    useEffect(() => {
        const token = localStorage.getItem("token");
        if (token) {
            getBooks();
        }
    }, [])



    return (
        <>
            <div className={styles.dashboard}>
                <div className={styles.search}>
                    <h1>Search the books available in Library</h1>
                    <div className={styles.searchbox}>
                        <input type="text" onChange={handleSearchInputChange} placeholder="Oddo Developement" />
                        <button className='button'>search</button>
                    </div>
                </div>


            </div>
            <div className="container mt-3">
                <div className="row">
                    <div className="col-lg-6">
                        <h1 className={styles.title}>New Arrivals</h1>
                        {books.length > 0 ? books.map((item, index) => {
                            return <Card index={index} data={item} />
                        }) : <p>No Books </p>}
                    </div>
                    <div className="col-lg-6">
                        <h1 className={styles.title}>Trending</h1>
                        {books.length > 0 ? books.map((item, index) => {
                            return <Card index={index} data={item} />
                        }) : <p>No Books </p>}
                    </div>
                </div>

            </div>
        </>
    )
}

export default Dashboard
