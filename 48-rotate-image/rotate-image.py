class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        """
        1. We can do transpose
        2. Reverse

        """
        n = len(matrix)

        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        for row in range(n):
            matrix[row].reverse()

