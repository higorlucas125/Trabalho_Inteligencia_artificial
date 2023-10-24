import "./App.css";
import TicToc from "./Components/TicToc";
import Home from "./Components/Home";
import Sidebar from "./Components/Sidebar";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import TicTocCpuVsCpu from "./Components/TicTocCpuVsCpu";
import TicTocCpuVsJogador from "./Components/TicTocCpuVsJogador";

function App() {
  return (
    <div className="App">
      <header className="grid-container">
        <BrowserRouter>
        <Sidebar/>
          <Routes>
            <Route index element={<Home />} />
            <Route path="/PlayerVsPlayer" element={<TicToc typeGame="PvsP"/>} />
            <Route path="/PlayerVsCPU" element={<TicTocCpuVsJogador/>} />
            <Route path="/CPUVsCPU" element={<TicTocCpuVsCpu typeGame="CpuVsCpu"/>} />
            
          </Routes>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
