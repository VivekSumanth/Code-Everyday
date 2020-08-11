class Rat_in_maze():
    
    def __init__(self,maze):
        self.maze = maze
        self.row = len(self.maze)
        self.col = len(self.maze[0])
        self.destination = [self.row,self.col]
        
    def start(self):
        self.route = ''
        self.dfs(0,0,'',self.maze)
        print(self.route)
    
    def dfs(self,row,col,route,maze):
        if row == self.destination[0] and col == self.destination[1]:
            
            return self.route

        elif row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == 0 :
            return 
        
        else:
            
            l = str(row) + str(col) +','
            k = maze[row][col]
            maze[row][col] = 0
            
            self.route =  route
            
            (self.dfs(row+1,col, route+l, maze) or self.dfs(row-1,col, route+l, maze) or self.dfs(row,col+1, route+l, maze) or self.dfs(row,col-1, route+l, maze))
            
            maze[row][col] = 1
            
           
        return self.route

maze = [ [1, 0, 0, 1],[1, 0, 0, 1],[1, 0, 0, 1],[1, 1, 1, 1] ] 
g = Rat_in_maze(maze)
g.start()