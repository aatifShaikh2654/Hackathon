import React, { useState } from 'react'
import StateContext from './StateContext'

const State = (props) => {

    const [loading, setLoading] = useState({ open: false, text: '' });
    const [books, setBooks] = useState({});
    
    
  return (
    <>
      <StateContext.Provider value={{ loading, setLoading, books, setBooks }}>
        {props.children}
      </StateContext.Provider>
    </>
  )
}

export default State
