

class Solution:
    def noRepeat(self, l):
        l = list(filter(lambda item: item != '.', l))
        return len(set(l)) == len(l)
    
    def getSubSudoku(self, board, r, c):
        return [board[r + i][c + j] for i in range(3) for j in range(3)]
    
    def checkEach(self, l):
        return all([self.noRepeat(item) for item in l])
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = board
        cols = [[board[i][j] for i in range(9)] for j in range(9)]
        subs = [self.getSubSudoku(board, i, j) for i in range(0, 9, 3) for j in range(0, 9, 3)]
        
        return self.checkEach(rows) and self.checkEach(cols) and self.checkEach(subs)


if __name__ == '__main__':
    def test(*args, **kwargs):
        print(*args, Solution().isValidSudoku(*args, **kwargs), **kwargs)
    
    
    test([["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]])