var resultComparacao ={
    row : '',
    columns : '',
    time: '',
    node: '',
    qtd: '',
    player:'',
    algoritmo:''
}


export const deepCopy = (item) => {
  return JSON.parse(JSON.stringify(item));
};

const jogadasPossiveis = (board) => {
  var jogadas = [];
  for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
      if (board[i][j] == "") jogadas.push([i, j]);
    }
  }
  return jogadas;
};

const jogada = (board, jogadorNova, jogadorAntigo) => {
  let copyBoard = deepCopy(board);
  copyBoard[jogadorNova[0]][jogadorNova[1]] = jogadorAntigo;
  return copyBoard;
};

const verificarSeEmpatou = (board) => {
  for (var row in board) {
    for (var col in board[row]) {
      if (board[row][col] == "") return false;
    }
  }
  return true;
};

const verificarQuemGanhou = (board) => {
  if( board[2][2] == board[0][2] && board[2][2] == board[1][2])
    return board[2][2];
  if (board[0][0] == board[0][1] && board[0][0] == board[0][2])
    return board[0][0];
  if (board[1][0] == board[1][1] && board[1][0] == board[1][2])
    return board[1][0];
  if (board[2][0] == board[2][1] && board[2][0] == board[2][2])
    return board[2][0];
  if (board[0][0] == board[1][0] && board[0][0] == board[2][0])
    return board[0][0];
  if (board[0][1] == board[1][1] && board[0][1] == board[2][1])
    return board[0][1];
  if (board[0][2] == board[1][2] && board[0][2] == board[2][2])
    return board[0][2];
  if (board[0][0] == board[1][1] && board[0][0] == board[2][2])
    return board[0][0];
  if (board[0][2] == board[1][1] && board[0][2] == board[2][0])
    return board[0][2];
  return null;
};


const potoDeParada = (board,jogadorAntigo) =>{
  let w = verificarQuemGanhou(board);
  if (w == jogadorAntigo) return 1;
  if (w && w != jogadorAntigo) return -1;
  if (!w && verificarSeEmpatou(board)) return 0;
}

export const minimax_alfa_beta = (
  board,
  jogadorNovo,
  jogadorAntigo,
  alpha,
  beta
) => {
  let parada = potoDeParada(board,jogadorAntigo);
  if(parada != null){
    return parada;
  }

  let jogadas = jogadasPossiveis(board);

  resultComparacao.qtd += 1;
  resultComparacao.player = jogadorNovo;

  if (jogadorNovo == jogadorAntigo) {
    let bestScore = -10;
    for (let i in jogadas) {
      let resultado = jogada(board, jogadas[i], jogadorNovo);
      let valor = minimax_alfa_beta(
        resultado,
        jogadorNovo == "X" ? "O" : "X",
        jogadorAntigo,
        alpha,
        beta
      );
      bestScore = Math.max(bestScore, valor);
      alpha = Math.max(alpha, bestScore);
      if (beta <= alpha) {
        break;
      }
    }
    return bestScore;
  } else {
    let bestScore = 10;
    for (let i in jogadas) {
      let resultado = jogada(board, jogadas[i], jogadorNovo);
      let valor = minimax_alfa_beta(
        resultado,
        jogadorNovo == "X" ? "O" : "X",
        jogadorAntigo,
        alpha,
        beta
      );
      bestScore = Math.min(bestScore, valor);
      beta = Math.min(beta, bestScore);
      if (beta <= alpha) {
        break;
      }
    }
    return bestScore;
  }
};

export const minimax = (board, jogadorNova, jogadorAntigo) => {
  
  let parada = potoDeParada(board,jogadorAntigo);
  if(parada != null){
    return parada;
  }

  // Codigo de recusividade aqui
  let jogadas = jogadasPossiveis(board);
  
  resultComparacao.qtd += 1;
  resultComparacao.player = jogadorNova;
  // Significa que ele é o X
  if (jogadorNova == jogadorAntigo) {
    //MAX
    let best = -10;
    for (let i in jogadas) {
      let resultado = jogada(board, jogadas[i], jogadorNova);
      let valor = minimax(
        resultado,
        jogadorNova == "X" ? "O" : "X",
        jogadorAntigo
      );
      if (valor > best) {
        best = valor;
      }
    }

    return best;
  } else {
    let best = 10;
    for (let i in jogadas) {
      let resultado = jogada(board, jogadas[i], jogadorNova);
      let valor = minimax(
        resultado,
        jogadorNova == "X" ? "O" : "X",
        jogadorAntigo
      );
      if (valor < best) {
        best = valor;
      }
    }

    return best;
  }
};

export const best = (board, jogadorAntigo, algoritmo) => {
  let jogadas = jogadasPossiveis(board);
  let best = -10;
  let posicaoJogada = null;
  resultComparacao.qtd = 0;
  let execution = new Date();

  resultComparacao.algoritmo = algoritmo.name;
  for (let i in jogadas) {
    let resultado = jogada(board, jogadas[i], jogadorAntigo);
    let valor = algoritmo(
      resultado,
      jogadorAntigo == "X" ? "O" : "X",
      jogadorAntigo,
      -10,
      10
    );
    //console.log(jogadas[i], i);
    //console.log(valor);
    resultComparacao.node = i;
    if (valor > best) {
      best = valor;
      posicaoJogada = jogadas[i];
      resultComparacao.row = posicaoJogada[0];
      resultComparacao.columns = posicaoJogada[1];
    }
    //console.log(resultado);
  }

  resultComparacao.time =  new Date() - execution + " ms";

  //console.log(resultComparacao)

  return {posicaoJogada,resultComparacao};
  // return posicaoJogada;

};
