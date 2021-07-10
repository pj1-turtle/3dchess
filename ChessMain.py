import pygame as p
import GameEngine

WIDTH = 1200
HEIGHT = 650
DIMENSION = 8
SQ_SIZE = 32
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ', 'wU', 'bU']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Note: we can access an image by saying 'IMAGES['wp']'

def main():
    
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = GameEngine.GameState()
    validMoves = gs.getValidMoves() #expensive operation to keep checking valid moves
    moveMade = False #flag variable for when a move is made, used to generate valid moves only when gamestate has been changed
    
    print(gs.board)
    loadImages()
    
    running = True
    cubeSelected = () #keep track of the last cube selected. (tuple: row, col, level)
    playerClicks = [] #keep track of player clicks, (2 tuples: [(4, 4, 1), (4, 4, 2)])

    
    
    while running:
        for e in p.event.get():
            
            if e.type == p.QUIT:
                running = False


            #mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                if (location[0] < 270):
                    if (location[1] < 270):
                        col = location[0]//SQ_SIZE
                        row = location[1]//SQ_SIZE
                        level = 0
                    elif (location[1] < 570):
                        col = (location[0])//SQ_SIZE
                        row = (location[1]-300)//SQ_SIZE
                        level = 4

                elif (location[0] < 570):
                    if (location[1] < 270):
                        col = (location[0]-300)//SQ_SIZE
                        row = location[1]//SQ_SIZE
                        level = 1
                    elif (location[1] < 570):
                        col = (location[0]-300)//SQ_SIZE
                        row = (location[1]-300)//SQ_SIZE
                        level = 5

                elif (location[0] < 870):
                    if (location[1] < 270):
                        col = (location[0]-600)//SQ_SIZE
                        row = location[1]//SQ_SIZE
                        level = 2
                    elif (location[1] < 570):
                        col = (location[0]-600)//SQ_SIZE
                        row = (location[1]-300)//SQ_SIZE
                        level = 6

                elif (location[0] < 1170):
                    if (location[1] < 270):
                        col = (location[0]-900)//SQ_SIZE
                        row = location[1]//SQ_SIZE
                        level = 3
                    elif (location[1] < 570):
                        col = (location[0]-900)//SQ_SIZE
                        row = (location[1]-300)//SQ_SIZE
                        level = 7

                if cubeSelected == (level, row, col):
                    cubeSelected = () #deselect
                    playerClicks = [] #clear player clicks
                else:
                    cubeSelected = (level, row, col)
                    playerClicks.append(cubeSelected)
                if(len(playerClicks) == 2): #after second click poggers, make a move
                    move = GameEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    print(move)
                    if (move in validMoves and moveMade == False):
                        if gs.whiteToMove:
                            if (move.endAisle, move.endRow, move.endCol) == (gs.blackKingLocation):
                                gs.WhiteWinscheckMate = True       
                                #must implement a reward here, something to stop the program from making any new moves                                                                               
                        else:
                            if(move.endAisle, move.endRow, move.endCol) == (gs.whiteKingLocation):
                                gs.BlackWinscheckMate = True

                        gs.makeMove(move)
                        moveMade = True

                    cubeSelected = ()
                    playerClicks = []


            #key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when z is pressed 
                    gs.undoMove()
                    moveMade = True
                
                    
                
        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState0(screen, gs)
        drawGameState1(screen, gs)
        drawGameState2(screen, gs)
        drawGameState3(screen, gs)
        drawGameState4(screen, gs)
        drawGameState5(screen, gs)
        drawGameState6(screen, gs)
        drawGameState7(screen, gs)
        clock.tick(MAX_FPS)
        
        p.display.flip()

def drawGameState0(screen, gs):
    colors = [p.Color(235, 235, 208), p.Color(119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[0], 0, 0)

    
def drawGameState1(screen, gs):
    colors = [p.Color(119, 148, 85), p.Color(235, 235, 208)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+300, (r*SQ_SIZE), SQ_SIZE, SQ_SIZE))

    drawPieces(screen, gs.board[1], 300, 0)
    

def drawGameState2(screen, gs):
    colors = [p.Color(235, 235, 208), p.Color(119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+600, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[2], 600, 0)

    
def drawGameState3(screen, gs):
    colors = [p.Color(119, 148, 85), p.Color(235, 235, 208)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+900, (r*SQ_SIZE), SQ_SIZE, SQ_SIZE))

    drawPieces(screen, gs.board[3], 900, 0)
    

def drawGameState4(screen, gs):
    colors = [p.Color(235, 235, 208), p.Color(119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, (r*SQ_SIZE)+300, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[4], 0, 300)

    
def drawGameState5(screen, gs):
    colors = [p.Color(119, 148, 85), p.Color(235, 235, 208)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+300, (r*SQ_SIZE)+300, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[5], 300, 300)

    
def drawGameState6(screen, gs):
    colors = [p.Color(235, 235, 208), p.Color(119, 148, 85)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+600, (r*SQ_SIZE)+300, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[6], 600, 300)

    
def drawGameState7(screen, gs):
    colors = [p.Color(119, 148, 85), p.Color(235, 235, 208)]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)]
            p.draw.rect(screen, color, p.Rect((c*SQ_SIZE)+900, (r*SQ_SIZE)+300, SQ_SIZE, SQ_SIZE))
            
    drawPieces(screen, gs.board[7], 900, 300)

    

def drawPieces(screen, boardFlat, number1, number2):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = boardFlat[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect((c*SQ_SIZE)+number1, (r*SQ_SIZE)+number2, SQ_SIZE, SQ_SIZE))
            
    
    
main()

















