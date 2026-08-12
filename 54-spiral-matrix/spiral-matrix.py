class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1. We create four boundaries
        2. top, bottom, left, right
        3. we just shrink the boundaries as we go
        4. First, we go through the top row
        5. we add top+=1 to shrink from top
        6. then we go through the right most column
        7. we shrink from right
        8. we go through the bottom most column from right to left
        9. we shrink bottom
        10. we go from bottom to up at left most side 
        11. we shrink left
        12. we keep doing that until top <= bottom and left <=right
        """

        top = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        left = 0

        result = []

        while top<=bottom and left <=right:

            for column in range(left, right+1):
                result.append(matrix[top][column])
            
            top+=1
            for row in range(top, bottom+1):
                result.append(matrix[row][right])

            right -=1

            if top<=bottom:
                for column in range(right, left-1, -1):
                    result.append(matrix[bottom][column])
                

                bottom -=1
            if left<=right:
                for row in range(bottom, top-1, -1):
                    result.append(matrix[row][left])
                
                left+=1
            

        return result
                