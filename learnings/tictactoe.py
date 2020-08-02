class TicTacToe:
    
    def __init__(self, board):
        self.board = board
        self.winmoves = [
            [[0,0],[0,1],[0,2]],
            [[1,0],[1,1],[1,2]],
            [[2,0],[2,1],[2,2]],
            [[0,0],[1,1],[2,2]],
            [[0,2],[1,1],[2,2]],
            [[0,0],[1,0],[2,0]],
            [[0,1],[1,1],[2,1]],
            [[0,2],[1,2],[2,2]]
            ]
        print(self.winmoves)
        print(self.board)
        self.x = self.getposition(1)
        self.o = self.getposition(0)
        print('X:',self.x)
        print('o:',self.o)
        
    def getposition(self,num):
        position = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == num:
                    position.append([i,j])
        return position
    
    def putposistion(self,num)
                    
        
        
        


g = TicTacToe([[0,'',''],[0,1,''],[1,'','']])