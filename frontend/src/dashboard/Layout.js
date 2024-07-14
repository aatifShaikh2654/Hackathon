import React, { useContext, useEffect } from 'react'
import { Outlet, useNavigate } from 'react-router-dom'
import Navbar from '../components/Navbar'
// import UserContext from '../context/user/UserContext'

const Layout = () => {

  return (
    <>
      <div className="main">
        <Navbar />
        <h1>hello</h1>
        <Outlet />
      </div>
    </>
  )
}

export default Layout
