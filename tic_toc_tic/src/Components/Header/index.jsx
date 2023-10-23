import React,{useContext} from 'react'
import AppContext from '../AppContext'

const Playing = () =>{
     
    const { currentChar } = useContext(AppContext)

    return (
        <div>Playing now: <span>{currentChar}</span></div>
    )
}

const Winner = ()  =>{
    const { winner } = useContext(AppContext)

    return (
        <div>Congratulations <span>{winner}</span>, you WON!</div>
    )
}

const End = () =>{
    return (
        <div>Game Over</div>
    )
}

const Header = () => {
    const {winner,gameOver} = useContext(AppContext)
    return(
        <div className="header">
        { !winner && !gameOver && <Playing /> }
        { gameOver && !winner && <End /> }
        { winner && <Winner /> }
    </div>
    )
}


export default Header