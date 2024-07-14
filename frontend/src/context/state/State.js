import React, { useState } from 'react'
import StateContext from './StateContext'

const State = (props) => {

    const [loading, setLoading] = useState({ open: false, text: '' });

    
  return (
    <>
      <StateContext.Provider value={{ loading, setLoading }}>
        {props.children}
      </StateContext.Provider>
    </>
  )
}

export default State
