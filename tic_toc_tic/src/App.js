import "./App.css";
import TicToc from "./Components/TicToc";
import Home from "./Components/Home";

import { BrowserRouter, Routes, Route } from "react-router-dom";
import TicTocCpuVsCpu from "./Components/TicTocCpuVsCpu";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <BrowserRouter>
          <Routes>
            <Route index element={<Home />} />
            <Route path="PlayerVsPlayer" element={<TicToc typeGame="PvsP"/>} />
            <Route path="PlayerVsCPU" element={<TicToc typeGame="PlayerVsCpu"/>} />
            <Route path="CPUVsCPU" element={<TicTocCpuVsCpu typeGame="CpuVsCpu"/>} />
          </Routes>
        </BrowserRouter>
      </header>
    </div>
  );
}

export default App;
