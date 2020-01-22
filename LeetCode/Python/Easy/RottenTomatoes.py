""" 994. Rotting Oranges
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.


Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""

# Use BFS, and increment minutes per level.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue, minutes = [], 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2: queue.append((y,x))

        # flag to indicate end of level
        queue.append((-1,-1))
        while len(queue) > 0:
            y,x = queue.pop(0);

            # if flag is encountered, next level is already completed
            # --> append another flag to end of queue and increment minutes
            if x == -1 and y == -1 and len(queue) != 0:
                minutes += 1
                queue.append((-1,-1))
                continue
            elif x == -1 and y == -1:
                break
            if y > 0 and grid[y-1][x] == 1:
                grid[y-1][x] = 2
                queue.append((y-1,x))
            if y < len(grid) - 1 and grid[y+1][x] == 1:
                grid[y+1][x] = 2
                queue.append((y+1,x))
            if x > 0 and grid[y][x-1] == 1:
                grid[y][x-1] = 2
                queue.append((y,x-1))
            if x < len(grid[y]) - 1 and grid[y][x+1] == 1:
                grid[y][x+1] = 2
                queue.append((y,x+1))
        
        # check if there are any fresh tomatoes left in the grid
        # if there are, they're unreachable
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1: return -1
        return minutes