import React from 'react'
import './index.css'
import { BsCart3, BsGrid1X2Fill, BsFillArchiveFill, BsFillGrid3X3GapFill, BsPeopleFill, BsListCheck, BsMenuButtonWideFill, BsFillGearFill } from 'react-icons/bs'
import { useNavigate } from 'react-router-dom'

const Sidebar = ({OpenSidebarToggle,OpenSidebar}) => {
  const navigate = useNavigate();
  return (
    <aside id="sidebar" className={OpenSidebarToggle ? "sidebar-responsive": ""}>
        <div className="sidebar-title">
            <div className="sidebar-brand">
                MiniMax e Alfa Beta
            </div>
            <span className="close-icon" onClick={OpenSidebar}>X</span>
        </div>

        <ul className='sidebar-list'>
        <li className="sidebar-list-item">
                <a onClick={() => {navigate('/'); console.log("asdfadf");}}>
                    <BsGrid1X2Fill className='icon'/>Dashboard
                </a>
            </li>
            <li className="sidebar-list-item">
                <a onClick={() => {navigate('/PlayerVsPlayer'); console.log("asdfadf");}}>
                    <BsFillGearFill className='icon'/>PlayerVsPlayer
                </a>
            </li>
            <li className="sidebar-list-item">
                <a onClick={() => navigate('/PlayerVsCPU')}>
                    <BsFillGearFill className='icon'/>PlayerVsCPU
                </a>
            </li>
            <li className="sidebar-list-item">
                <a onClick={() => navigate('/CPUVsCPU')}>
                    <BsFillGearFill className='icon'/>CPUVsCPU
                </a>
            </li>
        </ul>
    </aside>
  )
}

export default Sidebar