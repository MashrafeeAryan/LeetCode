class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        1. we go through the whole matrix and find whcih row and column has zeros
        2. we save the row and colum  in a set.
        3. we then loop through the matrix again and then see if the column or row is in the set.
        4. if it is,we make the whole orw and column zeores
        """


        zeros_row = set()
        zeros_col = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zeros_row.add(row)
                    zeros_col.add(col)
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row in zeros_row or col in zeros_col:
                    matrix[row][col] =0
        
        