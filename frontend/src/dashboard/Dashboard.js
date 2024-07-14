import React, { useState } from 'react'
import styles from '../styles/dashboard.module.css';
import Card from '../components/Card';

const Dashboard = () => {

    const [searchResults, setSearchResults] = useState('');
    

    const handleSearchInputChange = (event) => {
        const query = event.target.value;
        // Perform search/filtering logic
        // const filteredResults = products.filter(product =>
        //     product.fields.name.toLowerCase().includes(query.toLowerCase())
        // );
        // setSearchResults(filteredResults);
    };




    return (
        <>
            <div className={styles.dashboard}>
                <div className={styles.search}>
                    <h1>Search the books available in Library</h1>
                    <div className={styles.searchbox}>
                        <input type="text" placeholder="Oddo Developement" />
                        <button className='button'>search</button>
                    </div>
                </div>


            </div>
            <div className="container mt-3">
                <div className="row">
                    <div className="col-lg-6">
                        <h1 className={styles.title}>New Arrivals</h1>
                        <Card />
                    </div>
                    <div className="col-lg-6">
                        <h1 className={styles.title}>Trending</h1>
                        <Card />
                    </div>
                </div>

            </div>
        </>
    )
}

export default Dashboard
