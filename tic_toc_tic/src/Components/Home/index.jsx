import React from 'react'
import './index'
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>Página Inicial</h1>
      <nav>
        <ul>
          <li>
            <Link to="/PlayerVsPlayer">Jogador vs Jogador</Link>
          </li>
          <li>
            <Link to="/PlayerVsCPU">Jogador vs Maquina</Link>
          </li>
          <li>
            <Link to="/CPUVsCPU">Maquina vs Maquina</Link>
          </li>
          <li>
            <Link to="/usuario">Usuario</Link>
          </li>
        </ul>
      </nav>
    </div>
  )
}

export default Home;
