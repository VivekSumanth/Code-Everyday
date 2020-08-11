# 79. Word Search
# Medium

# 4046

# 194

# Add to List

# Share
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 

# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# Accepted
# 505,024
# Submissions
# 1,419,080

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        each = 0
        self.statement = False
        check = ''
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == self.word[0]:
                    
                    self.dfs(i,j,board,0,check)
                
        return self.statement
    
    def dfs(self,i,j,board,each,check):
        if self.word == check:
            self.statement = True
            
        elif i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or each >= len(self.word) or board[i][j] != self.word[each]:
            return
        else:
            l = board[i][j] 
            board[i][j] = "#"
            self.dfs(i+1,j,board,each+1,check+l)
            self.dfs(i-1,j,board,each+1,check+l)
            self.dfs(i,j+1,board,each+1,check+l)
            self.dfs(i,j-1,board,each+1,check+l)
            
            board[i][j] = l


class Solution(object):
    def dfs(self,row,col,board,check,count):
        if count == len(self.word):
            self.flag = True
            return True
            
        
        elif row<0 or col<0 or row >= len(board) or col >= len(board[0]) or  board[row][col] != self.word[count]:
            return False
        
        l = board[row][col] 
        board[row][col] = "#"
        
        self.flag = self.dfs(row+1,col,  board,check+l,count+1) or self.dfs(row-1,col,  board,check+l,count+1) or self.dfs(row,  col+1,board,check+l,count+1) or self.dfs(row,  col-1,board,check+l,count+1)
        
        board[row][col] = l
        return self.flag
    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.word = word
        self.flag = False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == self.word[0] and self.dfs(row,col,board,self.word[0],0):
                    return True
