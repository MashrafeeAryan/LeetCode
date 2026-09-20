class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        """
        U: We are given an array and we have to check if we replace(or remove) one element, then can we get a increasing order array
        M: Keep a counter for how many elements we are repalcing
        P: How do we see if one value is greater than other?
            - We can see if next value is greater than curr value. If not we do counter -1.
            1. loop through nums 
            2. if curr != len(nums)-1 and curr > curr + 1:
                counter-=1
            3. if counter <=0:
                return False
            4. let loop end: return True
        I: 
        R: 
        E: Space only one counter O(1) and one loop will be O(n) time complexity
        """

        counter = 1
        for num in range(len(nums)-1):
            if nums[num] > nums[num+1]:
                if num == 0 or nums[num-1] <= nums[num+1]:
                    nums[num] = nums[num+1]
                else:
                    nums[num+1] = nums[num]

                counter -=1
            
            if counter <0:
                return False
        
        return True