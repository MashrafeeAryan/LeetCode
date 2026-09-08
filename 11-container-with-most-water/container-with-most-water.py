class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The maximum height of volume will depdn on min(left, right)
        We will have two pointers: left and right
        the width will be right - left
        We have a while loop: left<=right
        We move left when heihgt is smaller than right
        and vice versa
        we sotre the max vol

        """

        maxVol = 0
        left = 0
        right = len(height)-1

        while left<= right:
            minHeight = min(height[left], height[right])
            width = right - left
            vol = width * minHeight
            maxVol = max(maxVol, vol)

            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
        
        return maxVol