from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        time = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        new_row < 0
                        or new_row >= len(grid)
                        or new_col < 0
                        or new_col >= len(grid[0])
                    ):
                        continue

                    if grid[new_row][new_col] != 1:
                        continue

                    grid[new_row][new_col] = 2
                    fresh -= 1
                    queue.append((new_row, new_col))

            time += 1

        if fresh > 0:
            return -1

        return time