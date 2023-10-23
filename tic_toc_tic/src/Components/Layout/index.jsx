import React from 'react'
import { Outlet, Link } from "react-router-dom";

const Layout = () => {
  return (
    <>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/blogs">PlayerVsPlayer</Link>
          </li>
          <li>
            <Link to="/contact">PlayerVsCPU</Link>
          </li>
          <li>
            <Link to="/contact">CPUvsCPU</Link>
          </li>
        </ul>
      </nav>

      <Outlet />
    </>
  )
}

export default Layout