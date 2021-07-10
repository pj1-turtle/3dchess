import numpy as np
import pygame as p
        
class GameState():
    def __init__(self):
        #the board is an 8x8x8 3d numpy array. each element has 2 letters, the first character represents the color of the piece, and the second character represents the type of the piece.
        #'K', 'Q', 'U', 'R', 'B', 'N', 'P'. '--' represents no piece. 
        self.board = np.zeros((8,8,8), dtype=object)
        self.board[0] = [
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wp", "wU", "--", "wN", "wN", "--", "wU", "wp"],
            ["wp", "--", "wR", "wB", "wB", "wR", "--", "wp"],
            ["wp", "wN", "wR", "wK", "wQ", "wR", "wN", "wp"],
            ["wp", "wN", "wB", "wQ", "wQ", "wB", "wN", "wp"],
            ["wp", "--", "wB", "wR", "wR", "wB", "--", "wp"],
            ["wp", "wU", "--", "wN", "wN", "--", "wU", "wp"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
        ]
        self.board[1] = [
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "wp", "wp", "wp", "wp", "wp", "wp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]
        self.board[2] = [
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ]
        
        self.board[3] = [
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "wN", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            
        ]
        self.board[4] = [
            ["bp", "bp", "--", "--", "--", "--", "bp", "bp"],
            ["bp", "bp", "--", "--", "--", "--", "bp", "bp"],
            ["bp", "bp", "--", "wK", "bK", "--", "bp", "bp"],
            ["--", "--", "--", "--", "bQ", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["bp", "bp", "--", "--", "--", "--", "bp", "bp"],
            ["bp", "bp", "--", "--", "--", "--", "bp", "bp"],
            ["bp", "bp", "--", "--", "--", "--", "bp", "bp"],
        ]
        self.board[5] = [
            ["wp", "wp", "--", "--", "--", "--", "--", "--"],
            ["wp", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "wB", "--", "--", "--", "--"],
            ["--", "--", "--", "wU", "--", "--", "--", "--"],
            ["--", "--", "--", "wp", "wp", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "wp", "wp"],
            ["wp", "--", "--", "--", "--", "--", "wp", "wp"],
            ["wp", "wp", "--", "--", "--", "--", "wp", "wp"],
        ]
        
        self.board[6] = [
            ["--", "--", "--", "--", "--", "--", "--", "--"], 
            ["--", "bp", "--", "bp", "bp", "bp", "bp", "--"],
            ["--", "bp", "bp", "bp", "bp", "bp", "bp", "--"],
            ["--", "bp", "bp", "bp", "bp", "bp", "bp", "--"],
            ["--", "bp", "bp", "bp", "bp", "bp", "bp", "--"],
            ["--", "bp", "bp", "bp", "bp", "bp", "bp", "--"],
            ["--", "bp", "bp", "bp", "bp", "bp", "bp", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
        ]
        
        self.board[7] = [
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["bp", "bU", "--", "bN", "bN", "--", "bU", "bp"],
            ["bp", "--", "bR", "bB", "bB", "bR", "--", "bp"],
            ["bp", "bN", "bR", "bK", "bQ", "bR", "bN", "bp"],
            ["bp", "bN", "bB", "bQ", "bQ", "bB", "bN", "bp"],
            ["bp", "--", "bB", "bR", "bR", "bB", "--", "bp"],
            ["bp", "bU", "--", "bN", "bN", "--", "bU", "bp"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
        ]
        self.whiteToMove = True
        self.moveFunctions = {'p': self.getPawnMoves, 'N': self.getKnightMoves, 'B': self.getBishopMoves, 'U': self.getUnicornMoves, 'R': self.getRookMoves,
                              'Q': self.getQueenMoves, 'K': self.getKingMoves}

        
        self.moveLog = []
        self.whiteKingLocation=(0, 3, 3)
        self.blackKingLocation=(7, 3, 3)
        self.WhiteWinscheckMate = False
        self.BlackWinscheckMate = False


    ''' Make move does not work for en passant, castles, and pawn promotion'''

    def makeMove(self, move):
        if(self.WhiteWinscheckMate or self.BlackWinscheckMate):
            raise Exception ("checkmate has occured!")
        self.board[move.startAisle][move.startRow][move.startCol] = "--"
        self.board[move.endAisle][move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move)
        self.whiteToMove = not self.whiteToMove
        #update the king's location if moved
        if move.pieceMoved == 'wK':
            self.whiteKingLocation = (move.endAisle, move.endRow, move.endCol)
        if move.pieceMoved == 'bK':
            self.blackKingLocation = (move.endAisle, move.endRow, move.endCol)

    '''Undo the last move made'''
    

    def undoMove(self):
        if len(self.moveLog) != 0: #make sure there is a move to undo in the first place you datti
            move = self.moveLog.pop()
            self.board[move.startAisle][move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endAisle][move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove #swap players
            
            if move.pieceMoved == 'wK':
                self.whiteKingLocation = (move.startAisle, move.startRow, move.startCol)
            if move.pieceMoved == 'bK':
                self.blackKingLocation = (move.startAisle, move.startRow, move.startCol)
            
            self.WhiteWinscheckMate = False
            self.BlackWinscheckMate = False




    

    '''
    All moves considering checks
    '''

    def getValidMoves(self):      
            #pseudocode
            #step 1: get all possible moves
            #step 2: for each possible move, check that it is valid by doing the following:
            #2a: make the move
            #2b: generate the list of possible moves for the opposing player
            #2c: see if any of the moves attack your king
            #2d: if your king is safe, the move is valid, add it to a list
            #step 3: return the list of valid moves only
        moves = self.getAllPossibleMoves()                    
        return moves
        
    '''
    All moves WITHOUT considering checks
    '''                
        

    def getAllPossibleMoves(self):
        moves = []

        
        for l in range(len(self.board)): #number of levels
            for r in range(len(self.board[l])): #number of ranks
                for c in range(len(self.board[l][r])): #number of files
                    turn = self.board[l][r][c][0] #returns first letter of element in loop
                    if(turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                        piece = self.board[l][r][c][1] #returns second letter of element in loop, so the piece identity
                        self.moveFunctions[piece](l, r, c, moves) 
                        

                        


        for r in moves:
            if r.isValid == False:
                moves.remove(r)
            
        return moves

    '''
    Get all the pawn moves for the pawn located at cube location, and add the moves to a list
    '''
    def getPawnMoves(self, l, r, c, moves):
        if self.whiteToMove:
            if self.board[l+1][r][c] == "--": #regular pawn advance
                moves.append(Move((l, r, c), (l+1, r, c), self.board))

            #side pawn moves
            if(r > 0):
                if(r < 7):
                    if(c > 0):
                        if (c < 7):                                        
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                        else:
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                else:
                    if(c > 0):
                        if (c < 7):
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                        else:
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                        if self.board[l][r-1][c] == "--":
                            moves.append(Move((l, r, c), (l, r-1, c), self.board))
                        if self.board[l][r][c+1] == "--":
                            moves.append(Move((l, r, c), (l, r, c+1), self.board))
            else:
                if(c > 0):
                    if (c < 7):
                        if self.board[l][r+1][c] == "--":
                            moves.append(Move((l, r, c), (l, r+1, c), self.board))
                        if self.board[l][r][c+1] == "--":
                            moves.append(Move((l, r, c), (l, r, c+1), self.board))
                        if self.board[l][r][c-1] == "--":
                            moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                        if self.board[l][r+1][c] == "--":
                            moves.append(Move((l, r, c), (l, r+1, c), self.board))
                        if self.board[l][r][c-1] == "--":
                            moves.append(Move((l, r, c), (l, r, c-1), self.board))
                else:
                    if self.board[l][r+1][c] == "--":
                        moves.append(Move((l, r, c), (l, r+1, c), self.board))
                    if self.board[l][r][c+1] == "--":
                        moves.append(Move((l, r, c), (l, r, c+1), self.board))      

            #pawn captures
            
            if(r > 0):
                if(r < 7):
                    if(c > 0):
                        if (c < 7):                                            
                            if self.board[l+1][r+1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                            if self.board[l+1][r-1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                            if self.board[l+1][r][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
                            if self.board[l+1][r][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                            if self.board[l+1][r+1][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
                            if self.board[l+1][r+1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
                            if self.board[l+1][r-1][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
                            if self.board[l+1][r-1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
                        else:
                            if self.board[l+1][r+1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
                            if self.board[l+1][r-1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
                            if self.board[l+1][r][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                            if self.board[l+1][r+1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                            if self.board[l+1][r-1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                    else:
                        if self.board[l+1][r+1][c][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                        if self.board[l+1][r-1][c][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                        if self.board[l+1][r-1][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
                        if self.board[l+1][r+1][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
                        if self.board[l+1][r][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
                else:
                    if(c > 0):
                        if (c < 7):
                            if self.board[l+1][r-1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                            if self.board[l+1][r-1][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
                            if self.board[l+1][r-1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
                            if self.board[l+1][r][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
                            if self.board[l+1][r][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                        else:
                            if self.board[l+1][r-1][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
                            if self.board[l+1][r-1][c][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                            if self.board[l+1][r][c-1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                    else:
                        if self.board[l+1][r-1][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
                        if self.board[l+1][r-1][c][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
                        if self.board[l+1][r][c+1][0] == 'b':
                                moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
            else:
                if(c > 0):
                    if (c < 7):
                        if self.board[l+1][r][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
                        if self.board[l+1][r][c-1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                        if self.board[l+1][r+1][c+1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
                        if self.board[l+1][r+1][c-1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
                        if self.board[l+1][r+1][c][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                    else:
                        if self.board[l+1][r+1][c-1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
                        if self.board[l+1][r+1][c][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                        if self.board[l+1][r][c-1][0] == 'b':
                            moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
                else:
                    if self.board[l+1][r+1][c][0] == 'b':
                        moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
                    if self.board[l+1][r+1][c+1][0] == 'b':
                        moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
                    if self.board[l+1][r][c+1][0] == 'b':
                        moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
        else:#black moves
            
            if self.board[l-1][r][c] == "--": #regular pawn advance
                moves.append(Move((l, r, c), (l-1, r, c), self.board))
                
            if(r > 0):
                if(r < 7):
                    if(c > 0):
                        if (c < 7):                                        
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                        else:
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                            if self.board[l][r+1][c] == "--":
                                moves.append(Move((l, r, c), (l, r+1, c), self.board))
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                else:
                    if(c > 0):
                        if (c < 7):
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c+1] == "--":
                                moves.append(Move((l, r, c), (l, r, c+1), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                        else:
                            if self.board[l][r-1][c] == "--":
                                moves.append(Move((l, r, c), (l, r-1, c), self.board))
                            if self.board[l][r][c-1] == "--":
                                moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                        if self.board[l][r-1][c] == "--":
                            moves.append(Move((l, r, c), (l, r-1, c), self.board))
                        if self.board[l][r][c+1] == "--":
                            moves.append(Move((l, r, c), (l, r, c+1), self.board))
            else:
                if(c > 0):
                    if (c < 7):
                        if self.board[l][r+1][c] == "--":
                            moves.append(Move((l, r, c), (l, r+1, c), self.board))
                        if self.board[l][r][c+1] == "--":
                            moves.append(Move((l, r, c), (l, r, c+1), self.board))
                        if self.board[l][r][c-1] == "--":
                            moves.append(Move((l, r, c), (l, r, c-1), self.board))
                    else:
                        if self.board[l][r+1][c] == "--":
                            moves.append(Move((l, r, c), (l, r+1, c), self.board))
                        if self.board[l][r][c-1] == "--":
                            moves.append(Move((l, r, c), (l, r, c-1), self.board))
                else:
                    if self.board[l][r+1][c] == "--":
                        moves.append(Move((l, r, c), (l, r+1, c), self.board))
                    if self.board[l][r][c+1] == "--":
                        moves.append(Move((l, r, c), (l, r, c+1), self.board))

                        
            if(r > 0):
                if(r < 7):
                    if(c > 0):
                        if (c < 7):                                            
                            if self.board[l-1][r+1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                            if self.board[l-1][r-1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                            if self.board[l-1][r][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
                            if self.board[l-1][r][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                            if self.board[l-1][r+1][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
                            if self.board[l-1][r+1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
                            if self.board[l-1][r-1][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
                            if self.board[l-1][r-1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
                        else:
                            if self.board[l-1][r+1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
                            if self.board[l-1][r-1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
                            if self.board[l-1][r][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                            if self.board[l-1][r+1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                            if self.board[l-1][r-1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                    else:
                        if self.board[l-1][r+1][c][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                        if self.board[l-1][r-1][c][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                        if self.board[l-1][r-1][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
                        if self.board[l-1][r+1][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
                        if self.board[l-1][r][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
                else:
                    if(c > 0):
                        if (c < 7):
                            if self.board[l-1][r-1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                            if self.board[l-1][r-1][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
                            if self.board[l-1][r-1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
                            if self.board[l-1][r][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
                            if self.board[l-1][r][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                        else:
                            if self.board[l-1][r-1][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
                            if self.board[l-1][r-1][c][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                            if self.board[l-1][r][c-1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                    else:
                        if self.board[l-1][r-1][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
                        if self.board[l-1][r-1][c][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
                        if self.board[l-1][r][c+1][0] == 'w':
                                moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
            else:
                if(c > 0):
                    if (c < 7):
                        if self.board[l-1][r][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
                        if self.board[l-1][r][c-1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                        if self.board[l-1][r+1][c+1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
                        if self.board[l-1][r+1][c-1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
                        if self.board[l-1][r+1][c][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                    else:
                        if self.board[l-1][r+1][c-1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
                        if self.board[l-1][r+1][c][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                        if self.board[l-1][r][c-1][0] == 'w':
                            moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
                else:
                    if self.board[l-1][r+1][c][0] == 'w':
                        moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
                    if self.board[l-1][r+1][c+1][0] == 'w':
                        moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
                    if self.board[l-1][r][c+1][0] == 'w':
                        moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
            
        

    ''' and for the rest of the pieces '''
    def getKnightMoves(self, l, r, c, moves):
        if(self.whiteToMove):
            try:
                if(self.board[l][r-2][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-2, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-2][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-2, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+2][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+2, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+2][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+2, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-1][c+2][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-1, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-1][c-2][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-1, c-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c-2][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+1, c-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c+2][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+1, c+2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l+1][r-2][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r-2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r+2][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r+2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r][c+2][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r][c-2][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r, c-2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l+2][r][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+2, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+2, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r+1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+2, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r-1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+2, r-1, c), self.board))
            except IndexError:
                pass


            try:
                if(self.board[l-1][r-2][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r-2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+2][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r+2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c+2][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c-2][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r, c-2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l-2][r][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-2, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-2, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r+1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-2, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r-1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-2, r-1, c), self.board))
            except IndexError:
                pass

        else:
            try:
                if(self.board[l][r-2][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-2, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-2][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-2, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+2][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+2, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+2][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+2, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-1][c+2][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-1, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r-1][c-2][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-1, c-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c-2][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+1, c-2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c+2][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+1, c+2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l+1][r-2][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r-2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r+2][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r+2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r][c+2][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r][c-2][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r, c-2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l+2][r][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+2, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+2, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r+1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+2, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+2][r-1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+2, r-1, c), self.board))
            except IndexError:
                pass


            try:
                if(self.board[l-1][r-2][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r-2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+2][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r+2, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c+2][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r, c+2), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c-2][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r, c-2), self.board))
            except IndexError:
                pass

            
            try:
                if(self.board[l-2][r][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-2, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-2, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r+1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-2, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-2][r-1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-2, r-1, c), self.board))
            except IndexError:
                pass
            

    def getBishopMoves(self, l, r, c, moves):
        bool1 = True
        bool2 = True
        bool3 = True
        bool4 = True
        bool5 = True
        bool6 = True
        bool7 = True
        bool8 = True
        bool9 = True
        bool10 = True
        bool11 = True
        bool12 = True
        bool13 = True
        bool14 = True
        bool15 = True
        bool16 = True
        if(self.whiteToMove):
            for i in range(l+1, 8):
                for j in range(r+1, 8):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool1:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool1 = False
                            if(self.board[i][j][k][0] == 'w'):
                                bool1 = False
                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool2:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool2 = False
                            if(self.board[i][j][m][0] == 'w'):
                                bool2 = False
                    m = 0
                j = 0
                m = 0
                k = 0

                for j in range(r-1, -1, -1):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool3:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool3 = False
                            if(self.board[i][j][k][0] == 'w'):
                                bool3 = False
                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool4:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool4 = False
                            if(self.board[i][j][m][0] == 'w'):
                                bool4 = False
                    m = 0

                j = 0
                m = 0
                k = 0
                
            i = 0
            j = 0
            k = 0
            m = 0
                        
            for i in range(l-1, 0, -1):
                for j in range(r+1, 8):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool5:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool5 = False
                            if(self.board[i][j][k][0] == 'w'):
                                bool5 = False

                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool6:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool6 = False
                            if(self.board[i][j][m][0] == 'w'):
                                bool6 = False

                    m = 0
                j = 0
                m = 0
                k = 0

                for j in range(r-1, -1, -1):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool7:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool7 = False
                            if(self.board[i][j][k][0] == 'w'):
                                bool7 = False

                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool8:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'b'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool8 = False
                            if(self.board[i][j][m][0] == 'w'):
                                bool8 = False
                    m = 0
                j = 0
                m = 0
                k = 0
            i = 0
            m = 0
            k = 0
            j = 0
        else:
            for i in range(l+1, 8):
                for j in range(r+1, 8):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool9:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool9 = False
                            if(self.board[i][j][k][0] == 'b'):
                                bool9 = False
                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool10:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool10 = False
                            if(self.board[i][j][m][0] == 'b'):
                                bool10 = False
                    m = 0

                j = 0
                m = 0
                k = 0

                for j in range(r-1, -1, -1):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool11:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool11 = False
                            if(self.board[i][j][k][0] == 'b'):
                                bool11 = False
                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool12:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool12 = False
                            if(self.board[i][j][m][0] == 'b'):
                                bool12 = False
                    m = 0

                j = 0
                m = 0
                k = 0
                
            i = 0
            j = 0
            k = 0
            m = 0
                        
            for i in range(l-1, 0, -1):
                for j in range(r+1, 8):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool13:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool13 = False
                            if(self.board[i][j][k][0] == 'b'):
                                bool13 = False

                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool14:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool14 = False
                            if(self.board[i][j][m][0] == 'b'):
                                bool14 = False

                    m = 0
                j = 0
                m = 0
                k = 0

                for j in range(r-1, -1, -1):
                    for k in range(c+1, 8):
                        if(abs(i-l) == abs(j-r) == abs(k-c)) and bool15:
                            if(self.board[i][j][k] == "--"):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                            if(self.board[i][j][k][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, k), self.board))
                                bool15 = False
                            if(self.board[i][j][k][0] == 'b'):
                                bool15 = False
                                

                    k = 0

                    for m in range(c-1, -1, -1):
                        if(abs(i-l) == abs(j-r) == abs(m-c)) and bool16:
                            if(self.board[i][j][m] == "--"):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                            if(self.board[i][j][m][0] == 'w'):
                                moves.append(Move((l, r, c), (i, j, m), self.board))
                                bool16 = False
                            if(self.board[i][j][m][0] == 'b'):
                                bool16 = False
                    m = 0
                j = 0
                m = 0
                k = 0
            i = 0
            m = 0
            k = 0
            j = 0
            
                                                                                        
    def getRookMoves(self, l, r, c, moves):
        if(self.whiteToMove):
            potentialL = []
            for j in range(l+1, 8):
                if(self.board[j][r][c] == "--"):
                    potentialL.append(j)
                    moves.append(Move((l, r, c), (j, r, c), self.board))
                if(self.board[j][r][c][0] == 'b'):
                    potentialL.append(j)
                    moves.append(Move((l, r, c), (j, r, c), self.board))
                    break
                if(self.board[j][r][c][0] == 'w'):
                    break
            for k in range(l-1, -1, -1):
                if(self.board[k][r][c] == "--"):
                    potentialL.append(k)
                    moves.append(Move((l, r, c), (k, r, c), self.board))
                if(self.board[k][r][c][0] == 'b'):
                    potentialL.append(k)
                    moves.append(Move((l, r, c), (k, r, c), self.board))
                    break
                if(self.board[k][r][c][0] == 'w'):
                    break

            potentialR = []
            for j in range(r+1, 8):
                if(self.board[l][j][c] == "--"):
                    potentialR.append(j)
                    moves.append(Move((l, r, c), (l, j, c), self.board))
                if(self.board[l][j][c][0] == 'b'):
                    potentialR.append(j)
                    moves.append(Move((l, r, c), (l, j, c), self.board))
                    break
                if(self.board[l][j][c][0] == 'w'):
                    break
            for k in range(r-1, -1, -1):
                if(self.board[l][k][c] == "--"):
                    potentialR.append(k)
                    moves.append(Move((l, r, c), (l, k, c), self.board))
                if(self.board[l][k][c][0] == 'b'):
                    potentialR.append(k)
                    moves.append(Move((l, r, c), (l, k, c), self.board))
                    break
                if(self.board[l][k][c][0] == 'w'):
                    break
            
            potentialC = []
            for j in range(c+1, 8):
                if(self.board[l][r][j] == "--"):
                    potentialC.append(j)
                    moves.append(Move((l, r, c), (l, r, j), self.board))
                if(self.board[l][r][j][0] == 'b'):
                    potentialC.append(j)
                    moves.append(Move((l, r, c), (l, r, j), self.board))
                    break
                if(self.board[l][r][j][0] == 'w'):
                    break
            for k in range(c-1, -1, -1):
                if(self.board[l][r][k] == "--"):
                    potentialC.append(k)
                    moves.append(Move((l, r, c), (l, r, k), self.board))
                if(self.board[l][r][k][0] == 'b'):
                    potentialC.append(k)
                    moves.append(Move((l, r, c), (l, r, k), self.board))
                    break
                if(self.board[l][r][k][0] == 'w'):
                    break
        else:
            blackpotentialL = []
            for j in range(l+1, 8):
                if(self.board[j][r][c] == "--"):
                    blackpotentialL.append(j)
                    moves.append(Move((l, r, c), (j, r, c), self.board))
                if(self.board[j][r][c][0] == 'w'):
                    blackpotentialL.append(j)
                    moves.append(Move((l, r, c), (j, r, c), self.board))
                    break
                if(self.board[j][r][c][0] == 'b'):
                    break
            for k in range(l-1, -1, -1):
                if(self.board[k][r][c] == "--"):
                    blackpotentialL.append(k)
                    moves.append(Move((l, r, c), (k, r, c), self.board))
                if(self.board[k][r][c][0] == 'w'):
                    blackpotentialL.append(k)
                    moves.append(Move((l, r, c), (k, r, c), self.board))
                    break
                if(self.board[k][r][c][0] == 'b'):
                    break

            blackpotentialR = []
            for j in range(r+1, 8):
                if(self.board[l][j][c] == "--"):
                    blackpotentialR.append(j)
                    moves.append(Move((l, r, c), (l, j, c), self.board))
                if(self.board[l][j][c][0] == 'w'):
                    blackpotentialR.append(j)
                    moves.append(Move((l, r, c), (l, j, c), self.board))
                    break
                if(self.board[l][j][c][0] == 'b'):
                    break
            for k in range(r-1, -1, -1):
                if(self.board[l][k][c] == "--"):
                    blackpotentialR.append(k)
                    moves.append(Move((l, r, c), (l, k, c), self.board))
                if(self.board[l][k][c][0] == 'w'):
                    blackpotentialR.append(k)
                    moves.append(Move((l, r, c), (l, k, c), self.board))
                    break
                if(self.board[l][k][c][0] == 'b'):
                    break
            
            blackpotentialC = []
            for j in range(c+1, 8):
                if(self.board[l][r][j] == "--"):
                    blackpotentialC.append(j)
                    moves.append(Move((l, r, c), (l, r, j), self.board))
                if(self.board[l][r][j][0] == 'b'):
                    blackpotentialC.append(j)
                    moves.append(Move((l, r, c), (l, r, j), self.board))
                    break
                if(self.board[l][r][j][0] == 'w'):
                    break
            for k in range(c-1, -1, -1):
                if(self.board[l][r][k] == "--"):
                    blackpotentialC.append(k)
                    moves.append(Move((l, r, c), (l, r, k), self.board))
                if(self.board[l][r][k][0] == 'b'):
                    blackpotentialC.append(k)
                    moves.append(Move((l, r, c), (l, r, k), self.board))
                    break
                if(self.board[l][r][k][0] == 'w'):
                    break
            
            
                                
    def getUnicornMoves(self, l, r, c, moves):
        bool17 = True
        bool18 = True
        bool19 = True
        bool20 = True
        bool21 = True
        bool22 = True
        bool23 = True
        bool24 = True
        bool25 = True
        bool26 = True
        bool27 = True
        bool28 = True

        bool29 = True
        bool30 = True
        bool31 = True
        bool32 = True
        bool33 = True
        bool34 = True
        bool35 = True
        bool36 = True
        bool37 = True
        bool38 = True
        bool39 = True
        bool40 = True
        if(self.whiteToMove):
            for j in range(r+1, 8):
                for k in range(c+1, 8):
                    if(abs(j-r) == abs(k-c)) and bool17:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'b'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool17 = False
                        if(self.board[l][j][k][0] == 'w'):
                            bool17 = False

                k = 0
                for k in range(c-1, -1, -1):
                    if(abs(j-r) == abs(k-c)) and bool18:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'b'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool18 = False
                        if(self.board[l][j][k][0] == 'w'):
                            bool18 = False
                k = 0
            j = 0
            k = 0 
            for j in range(r-1, -1, -1):
                for k in range(c+1, 8):
                    if(abs(j-r) == abs(k-c)) and bool19:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'b'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool19 = False
                        if(self.board[l][j][k][0] == 'w'):
                            bool19 = False

                k = 0
                for k in range(c-1, -1, -1):
                    if(abs(j-r) == abs(k-c)) and bool20:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'b'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool20 = False
                        if(self.board[l][j][k][0] == 'w'):
                            bool20 = False
                k = 0
            j = 0
            k = 0


            for i in range(l+1, 8):
                for j in range(r+1, 8):
                    if(abs(j-r) == abs(i-l)) and bool21:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'b'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool21 = False
                        if(self.board[i][j][c][0] == 'w'):
                            bool21 = False
                j = 0
                    
                for j in range(r-1, -1, -1):
                    if(abs(j-r) == abs(i-l)) and bool22:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'b'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool22 = False
                        if(self.board[i][j][c][0] == 'w'):
                            bool22 = False
                j = 0
            j = 0
            i = 0
            for i in range(l-1, -1, -1):
                for j in range(r+1, 8):
                    if(abs(j-r) == abs(i-l)) and bool23:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'b'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool23 = False
                        if(self.board[i][j][c][0] == 'w'):
                            bool23 = False
                j = 0
                    
                for j in range(r-1, -1, -1):
                    if(abs(j-r) == abs(i-l)) and bool24:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'b'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool24 = False
                        if(self.board[i][j][c][0] == 'w'):
                            bool24 = False
                j = 0
            j = 0
            i = 0

            for i in range(l+1, 8):
                for k in range(c+1, 8):
                    if(abs(k-c) == abs(i-l)) and bool25:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'b'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool25 = False
                        if(self.board[i][r][k][0] == 'w'):
                            bool25 = False

                k = 0
                
                for k in range(c-1, -1, -1):
                    if(abs(k-c) == abs(i-l)) and bool26:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'b'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool26 = False
                        if(self.board[i][r][k][0] == 'w'):
                            bool26 = False

                k = 0
            i = 0
            k = 0
            for i in range(l-1, -1, -1):
                for k in range(c+1, 8):
                    if(abs(k-c) == abs(i-l)) and bool27:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'b'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool27 = False
                        if(self.board[i][r][k][0] == 'w'):
                            bool27 = False

                k = 0
                
                for k in range(c-1, -1, -1):
                    if(abs(k-c) == abs(i-l)) and bool28:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'b'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool28 = False
                        if(self.board[i][r][k][0] == 'w'):
                            bool28 = False
                k = 0
            i = 0
            k = 0


            
        else:
            for j in range(r+1, 8):
                for k in range(c+1, 8):
                    if(abs(j-r) == abs(k-c)) and bool29:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'w'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool29 = False
                        if(self.board[l][j][k][0] == 'b'):
                            bool29 = False

                k = 0
                for k in range(c-1, -1, -1):
                    if(abs(j-r) == abs(k-c)) and bool30:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'w'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool30 = False
                        if(self.board[l][j][k][0] == 'b'):
                            bool30 = False
                k = 0
            j = 0
            k = 0 
            for j in range(r-1, -1, -1):
                for k in range(c+1, 8):
                    if(abs(j-r) == abs(k-c)) and bool31:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'w'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool31 = False
                        if(self.board[l][j][k][0] == 'b'):
                            bool31 = False

                k = 0
                for k in range(c-1, -1, -1):
                    if(abs(j-r) == abs(k-c)) and bool32:
                        if(self.board[l][j][k] == "--"):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                        if(self.board[l][j][k][0] == 'w'):
                            moves.append(Move((l, r, c), (l, j, k), self.board))
                            bool32 = False
                        if(self.board[l][j][k][0] == 'b'):
                            bool32 = False
                k = 0
            j = 0
            k = 0


            for i in range(l+1, 8):
                for j in range(r+1, 8):
                    if(abs(j-r) == abs(i-l)) and bool33:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'w'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool33 = False
                        if(self.board[i][j][c][0] == 'b'):
                            bool33 = False
                j = 0
                    
                for j in range(r-1, -1, -1):
                    if(abs(j-r) == abs(i-l)) and bool34:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'w'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool34 = False
                        if(self.board[i][j][c][0] == 'b'):
                            bool34 = False
                j = 0
            j = 0
            i = 0
            for i in range(l-1, -1, -1):
                for j in range(r+1, 8):
                    if(abs(j-r) == abs(i-l)) and bool35:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'w'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool35 = False
                        if(self.board[i][j][c][0] == 'b'):
                            bool35 = False
                j = 0
                    
                for j in range(r-1, -1, -1):
                    if(abs(j-r) == abs(i-l)) and bool36:
                        if(self.board[i][j][c] == "--"):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                        if(self.board[i][j][c][0] == 'w'):
                            moves.append(Move((l, r, c), (i, j, c), self.board))
                            bool36 = False
                        if(self.board[i][j][c][0] == 'b'):
                            bool36 = False
                j = 0
            j = 0
            i = 0

            for i in range(l+1, 8):
                for k in range(c+1, 8):
                    if(abs(k-c) == abs(i-l)) and bool37:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'w'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool37 = False
                        if(self.board[i][r][k][0] == 'b'):
                            bool37 = False

                k = 0
                
                for k in range(c-1, -1, -1):
                    if(abs(k-c) == abs(i-l)) and bool38:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'w'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool38 = False
                        if(self.board[i][r][k][0] == 'b'):
                            bool38 = False

                k = 0
            i = 0
            k = 0
            for i in range(l-1, -1, -1):
                for k in range(c+1, 8):
                    if(abs(k-c) == abs(i-l)) and bool39:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'w'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool39 = False
                        if(self.board[i][r][k][0] == 'b'):
                            bool39 = False

                k = 0
                
                for k in range(c-1, -1, -1):
                    if(abs(k-c) == abs(i-l)) and bool40:
                        if(self.board[i][r][k] == "--"):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                        if(self.board[i][r][k][0] == 'w'):
                            moves.append(Move((l, r, c), (i, r, k), self.board))
                            bool40 = False
                        if(self.board[i][r][k][0] == 'b'):
                            bool40 = False
                k = 0
            i = 0
            k = 0
                            

    def getQueenMoves(self, l, r, c, moves):
        self.getRookMoves(l, r, c, moves)
        self.getBishopMoves(l, r, c, moves)
        self.getUnicornMoves(l, r, c, moves)

    def getKingMoves(self, l, r, c, moves):
        
        if(self.whiteToMove):
            try: 
                if(self.board[l][r+1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r+1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r+1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-1, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r-1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l, r, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r-1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r-1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r-1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l-1][r][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c+1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c-1][0] != 'w'):
                    moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
            except IndexError:
                pass
        else:
            try: 
                if(self.board[l][r+1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r+1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l][r+1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r+1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-1, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r-1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r-1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l][r][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l, r, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r+1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r+1, c+1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r+1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r+1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r-1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r-1, c), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l+1][r-1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r-1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l+1][r-1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l+1, r-1, c-1), self.board))
            except IndexError:
                pass
            try: 
                if(self.board[l-1][r][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r+1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r+1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r+1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r+1, c-1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r-1, c), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c+1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r-1, c+1), self.board))
            except IndexError:
                pass
            try:
                if(self.board[l-1][r-1][c-1][0] != 'b'):
                    moves.append(Move((l, r, c), (l-1, r-1, c-1), self.board))
            except IndexError:
                pass

    
                                                        

class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}
    levelsToAisles = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    aislesToLevels = {v: k for k, v in levelsToAisles.items()}
    
    def __init__(self, startCube, endCube, board):
        self.startRow = startCube[1]
        self.startCol = startCube[2]
        self.startAisle = startCube[0]
        self.endRow = endCube[1]
        self.endCol = endCube[2]
        self.endAisle = endCube[0]
        self.isValid = True
        if(self.startRow < 0 or self.startRow > 7 or self.startCol < 0 or self.startCol > 7 or self.startAisle < 0 or self.startAisle > 7):
            isValid = False

        self.pieceMoved = board[self.startAisle][self.startRow][self.startCol]
        self.pieceCaptured = board[self.endAisle][self.endRow][self.endCol]
        
        self.moveID = (self.startAisle * 100000 + self.startRow * 10000 + self.startCol * 1000 + self.endAisle * 100 + self.endRow * 10 + self.endCol * 1) #creates unique number for every move

    '''Overriding the equals method'''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False
            
        
        

    def getChessNotation(self):
        return self.getRankFileLevel(self.startAisle, self.startRow, self.startCol) + self.getRankFileLevel(self.endAisle, self.endRow, self.endCol)

    def getRankFileLevel(self, l, r, c):        
        return self.aislesToLevels[l]+self.rowsToRanks[r]+self.colsToFiles[c]























    
    

            
            
        
