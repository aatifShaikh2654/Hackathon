import React, { useState } from 'react'
import StateContext from './StateContext'

const State = (props) => {

    const [loading, setLoading] = useState({ open: false, text: '' });
    const [books, setBooks] = useState({});
    const [updateBook, setUpdateBook] = useState({open: false, isbn: ''});
    
    
  return (
    <>
      <StateContext.Provider value={{ loading, setLoading, books, setBooks, updateBook, setUpdateBook }}>
        {props.children}
      </StateContext.Provider>
    </>
  )
}

export default State
