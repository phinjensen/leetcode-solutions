class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        if board[r][c] == 'E':
            adjacent = self.adjacent(board, r, c)
            count = sum(board[i][j] == 'M' for i, j in adjacent)
            if count > 0:
                board[r][c] = str(count)
            else:
                board[r][c] = 'B'
                for i, j in adjacent:
                    if board[i][j] == 'E':
                        self.updateBoard(board, [i, j])
        return board
    
    def adjacent(self, board, r, c):
        return [
            (i, j) for i, j in (
                (r,c-1),
                (r,c+1),
                (r-1,c),
                (r+1,c),
                (r+1,c+1),
                (r+1,c-1),
                (r-1,c+1),
                (r-1,c-1),
            ) if 0 <= i < len(board) and 0 <= j < len(board[0])
        ]
