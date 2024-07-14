import React, { useContext, useEffect, useState } from 'react'
import styles from '../styles/dashboard.module.css';
import Card from '../components/Card';
import StateContext from '../context/state/StateContext';
import UserContext from '../context/user/UserContext';

const Dashboard = () => {

    const [searchResults, setSearchResults] = useState([]);
    const { books } = useContext(StateContext);
    const { getBooks, trending, arrival, otherBooks, } = useContext(UserContext)

    const handleSearchInputChange = (event) => {
        const query = event.target.value.toLowerCase();
        // Perform search/filtering logic
        const filteredResults = books.filter(book =>
            book.title.toLowerCase().includes(query) ||
            book.author.toLowerCase().includes(query) ||
            book.genre.toLowerCase().includes(query)
        );
        setSearchResults(filteredResults);
        if (filteredResults == 0) {
            setSearchResults([])
        }
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
                        <button className='button' onClick={() => {searchResults([])}}>{searchResults.length > 0 ? 'cancel' : 'search'}</button>
                    </div>
                </div>


            </div>
            <div className="container mt-3">
                {searchResults.length == 0 ? <div className="row">
                    <div className="col-lg-6">
                        <h1 className={styles.title}>New Arrivals</h1>
                        {trending.length > 0 ? trending.slice(0, 5).map((item, index) => {
                            return <Card index={index} data={item} />
                        }) : <p>No Books </p>}
                    </div>
                    <div className="col-lg-6">
                        <h1 className={styles.title}>Trending</h1>
                        {arrival.length > 0 ? arrival.slice(0, 5).map((item, index) => {
                            return <Card index={index} data={item} />
                        }) : <p>No Books </p>}
                    </div>
                    <div className="col-12">
                        <h1>All Books</h1>
                        {otherBooks.length > 0 ? otherBooks.slice(0, 5).map((item, index) => {
                            return <Card index={index} data={item} />
                        }) : <p>No Books </p>}
                    </div>
                </div> :
                    null
                }

                {searchResults.length == 0 ? <div className="col-12">
                    {searchResults.length > 0 ? searchResults.slice(0, 5).map((item, index) => {
                        return <Card index={index} data={item} />
                    }) : <p>No Books </p>}
                </div> : null}

            </div>
        </>
    )
}

export default Dashboard
