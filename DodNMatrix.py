"""A dog is located at the top-left corner of an M X N grid (represented by a 2D matrix). A bone is placed at the bottom-right corner of the grid. 
The dog is allowed to move only in two directions at any point in time: Right or Down.In some scenarios, the grid contains obstacles (represented by 1) that the dog cannot pass through.
Empty paths are represented by 0.The goal is to calculate the total number of unique paths the dog can take from the start (0, 0) to the destination (M-1, N-1) 
Constraints & Rules
Movement: Only (i, j+1)(Right) or (i+1, j)(Down).
Grid Size: M X N where M, N = 1.
Obstacles: If a cell is 1, the number of paths through that cell is 0.
Edge Cases: If the starting point or ending point contains an obstacle, the total paths should be 0."""

def path(mat):
    rows = len(mat)
    cols = len(mat[0])
    memo  = {}
    
    def dfs(r,c):
        if r < 0 or c < 0 or mat[0][0] == 1:
            return 0
        if r == 0 and c == 0:
            return 1
        if (r,c) in memo:
            return memo[(r,c)]
            
        memo[(r,c)] = dfs(r-1,c) + dfs(r,c-1)
        
        return memo[(r,c)]
        
    return dfs(rows-1,cols-1)
    
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]]

print("Total unique path: ",path(grid))
