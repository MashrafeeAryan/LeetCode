class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1. have a maxVol = 0, variable
        2. Two pointers. one from left and one from right.
        3. We compare both and take the shorter height and multiply by the distane of right-left
        4. We then just check for the maxVol and store
        """

        right = len(height) -1
        left = 0
        maxVol = 0
        while left < right:
            distance = right - left
            current_height = min(height[left], height[right])
            area = current_height * distance
            maxVol = max(maxVol, area)

            if height[left] <= height[right]:
                left +=1
            else:
                right-=1
        return maxVol
