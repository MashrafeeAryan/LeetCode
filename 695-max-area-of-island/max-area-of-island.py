class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])


        def dfs(row, col):
            if(
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] ==0
            ):
                return 0


            grid[row][col] = 0
            area = 1

            area+= dfs(row, col+1)
            area+= dfs(row, col-1)
            area+= dfs(row+1, col)
            area+= dfs(row-1, col)
        
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col)
                    maxArea = max(maxArea, area)
        
        return maxArea
