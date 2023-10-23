import "./index.css"

import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import AppContext from "../AppContext";
import Cell from "../Cell";
import Header from "../Header";

const TicToc = (props) => {
    
    const empytGame = [["","",""],["","",""],["","",""]];
    const [cells,setCells] = useState(empytGame);
    const [winnerCells,setWinnerCells] = useState([[],[],[]]);
    
    const X = "X";
    const O = "O";

    const [currentChar,setCurrentChar] = useState(X)
    const [winner,setWinner] = useState("")
    const [gameOver,setGameOver] = useState(false)

    useEffect(() =>{
        isGameOver()
    },[cells])

    const cellClick = (row,column) => {
        if(gameOver || winner){
            return;
        }

        if(cells[row][column] != ""){
            return;
        }

        const newBoard = {...cells}
        newBoard[row][column] = currentChar
        console.log(newBoard);
        setCells(newBoard)
        changeChar()
    }


    const changeChar = () =>{
        if(currentChar == X){
            console.log("Passa aqui " + currentChar)
            setCurrentChar(O)
            console.log("Passa aqui Update" + currentChar)
        }else {
            setCurrentChar(X)
        }
    }

    const reset = () =>{
        setCells(empytGame)
        setWinner("")
        setGameOver(false)
        setWinnerCells([[],[],[]])
        setCurrentChar(X)
    }

    const isGameOver= () =>{
        switch (true) {
            case areTheSameInRow(0): return
            case areTheSameInRow(1): return
            case areTheSameInRow(2): return
            case areTheSameInColumn(0): return
            case areTheSameInColumn(1): return
            case areTheSameInColumn(2): return
            case areTheSameInDiagonal(): return
          }
        if (!cells[0].includes("") && !cells[1].includes("") && !cells[2].includes("")) {
            endGame("")
        }

    }

    const endGame = (winner) =>{
        if(winner != "") setWinner(winner)
        setGameOver(true)
    }

    const areTheSameInRow = (row) =>{
        if (cells[row][0] !== "" && cells[row][0] === cells[row][1] && cells[row][0] === cells[row][2]) {
            endGame(cells[row][0])
            
            const newWinner = [[],[],[]]
            newWinner[row][0] = true
            newWinner[row][1] = true
            newWinner[row][2] = true
            setWinnerCells(newWinner)
            return true
          }
        return false
    }

    const areTheSameInColumn= (column) =>{
        if (cells[0][column] !== "" && cells[0][column] === cells[1][column] && cells[2][column] == cells[0][column]) {
            endGame(cells[0][column])
            
            const newWinner = [[],[],[]]
            newWinner[0][column] = true
            newWinner[1][column] = true
            newWinner[2][column] = true
            setWinnerCells(newWinner)
            return true
          }
        return false
    }

    const areTheSameInDiagonal = () => {
        if (cells[1][1] != "" && (cells[0][0] === cells[1][1] && cells[0][0] == cells[2][2])) {
            endGame(cells[1][1])
            const newWinner = [[],[],[]]
            newWinner[0][0] = true
            newWinner[1][1] = true
            newWinner[2][2] = true
            setWinnerCells(newWinner)
            return true
        }
      
        if (cells[1][1] != "" && (cells[2][0] === cells[1][1] && cells[2][0] == cells[0][2])) {
            endGame(cells[1][1])
            const newWinner = [[],[],[]]
            newWinner[0][2] = true
            newWinner[1][1] = true
            newWinner[2][0] = true
            setWinnerCells(newWinner)
            return true
        }
        return false
    }
      
  return (
    <div>
    <AppContext.Provider value={{cells,setCells,setCurrentChar,cellClick,changeChar,currentChar,winner,gameOver,winnerCells}}>
        <Header></Header>
        <div className="board">
            <Cell row={0} column={0}></Cell>
            <Cell row={0} column={1}></Cell>
            <Cell row={0} column={2}></Cell>

            <Cell row={1} column={0}></Cell>
            <Cell row={1} column={1}></Cell>
            <Cell row={1} column={2}></Cell>

            <Cell row={2} column={0}></Cell>
            <Cell row={2} column={1}></Cell>
            <Cell row={2} column={2}></Cell>
        </div>
    </AppContext.Provider>
    <button className="btn-reset" onClick={() =>{ reset()}}>Reset</button>
    <Link to="/">Voltar</Link>
    </div>
  )
}

export default TicToc

