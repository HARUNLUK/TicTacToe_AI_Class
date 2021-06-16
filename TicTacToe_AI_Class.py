"""
Tic Tac Toe Player
"""

import math
import random
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board is None:
        raise NotImplementedError
        return
    counter=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=="X":
                counter+=1
            elif board[i][j]=="O":
                counter-=1
    if counter>0:
        return O
    elif counter<=0:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions=list()
    if board is None:
        raise NotImplementedError
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions.append((i,j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board is None:
        raise NotImplementedError
    if actions is None:
        return None
    whichPlayer=player(board)
    newBoard =  [[EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]
    if board[action[0]][action[1]] is EMPTY:
        for i in range(3):
            for j in range(3):
                if(board[i][j]==None):
                    newBoard[i][j] = EMPTY
                else:
                    newBoard[i][j] = str(board[i][j])
    else:
        raise ValueError
        return
    newBoard[action[0]][action[1]]=whichPlayer
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board is None:
        raise NotImplementedError
    if player(board)==X:
        whichPlayer=O
    else:
        whichPlayer=X
    for i in range(3):
        if board[i][0]==whichPlayer and board[i][1]==whichPlayer and board[i][2]==whichPlayer:
            return whichPlayer
        if board[0][i]==whichPlayer and board[1][i]==whichPlayer and board[2][i]==whichPlayer:
            return whichPlayer
    if board[0][0]==whichPlayer and board[1][1]==whichPlayer and board[2][2]==whichPlayer:
        return whichPlayer
    if board[0][2]==whichPlayer and board[1][1]==whichPlayer and board[2][0]==whichPlayer:
        return whichPlayer
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if board is None:
        raise NotImplementedError
    isOver=True
    if winner(board) is not None:
        isOver=True
    else:
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    isOver = False
    return isOver

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board is None:
        raise NotImplementedError
    if terminal(board):
        winnerPlayer = winner(board)
        if winnerPlayer == X:
            return 1
        elif winnerPlayer == O:
            return -1
        else:
            return 0
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if board is None:
        raise NotImplementedError
    if terminal(board):
        return None
    moves=actions(board)
    bestMoves=list()
    point=0
    for i in range(len(moves)):
        newBoard=result(board,moves[i])
        subPoint=subPoints(newBoard)
        if player(board)==X:
            if subPoint > point:
                point = utility(newBoard)
                bestMoves.clear()
                bestMoves.append(moves[i])
            elif subPoint == point:
                bestMoves.append(moves[i])
            newBoard[moves[i][0]][moves[i][1]]=O
            if utility(newBoard)==-1:
                return moves[i]
        else:
            if subPoint < point:
                point = utility(newBoard)
                bestMoves.clear()
                bestMoves.append(moves[i])
            elif subPoint == point:
                bestMoves.append(moves[i])
            newBoard[moves[i][0]][moves[i][1]]=X
            if utility(newBoard)==1:
                return moves[i]
    if not bestMoves:
        return moves[random.randrange(0, len(moves))]
    return bestMoves[random.randrange(0, len(bestMoves))]
def subPoints(board):
    if terminal(board):
        return utility(board)
        
    moves=actions(board)
    sum=0
    for i in range(len(moves)):
        sum+=subPoints(result(board,moves[i]))
    return sum
              


