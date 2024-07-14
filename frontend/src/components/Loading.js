import React, { useContext } from 'react'
import StateContext from '../context/state/StateContext'

const Loading = () => {
    
    const { loading } = useContext(StateContext);

    return (
        <>
            {loading.open ? <div className="loading">
                <div className="back-drop"></div>
                <div className="loading-content">
                    <svg viewBox="25 25 50 50" className='loading-svg'>
                        <circle r="20" cy="50" cx="50"></circle>
                    </svg>
                    <span>{loading.text}</span>
                </div>
            </div> : null}
        </>
    )
}

export default Loading
