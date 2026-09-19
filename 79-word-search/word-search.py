class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        U: We have a grid of characters. We needd to find the word in the grid. The character of the word hve to be sequential horizontally or vertically. 
        M: Similar to the islands problems where you look above down left and right. we here look just down and right. So dfs?
        Recursion
        P: We find the first letter of the word in grid, then we look for the second letter down or right. If we find it, we move on to next character and do the same. If not, we find another instance of the first letter of the word and try it again
        """

        def dfs(r, c, i):
                        
            if i == len(word):
                return True

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            
            if board[r][c] != word[i]:
                return False


            temp_letter = board[r][c]

            #Mark the letter
            board[r][c] = "#"

            found = (
            dfs(r-1, c, i+1) or
            dfs(r+1, c, i+1) or
            dfs(r, c+1, i+1) or
            dfs(r, c-1, i+1)
            )

            board[r][c] = temp_letter

            return found
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True
        
        return False
