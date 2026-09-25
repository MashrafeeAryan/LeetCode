class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        U: We are returning the index of a peak element. Peak element means the element is greater than it's neighbors. So in simple terms, if n = peak element. n is greater than n-1 and n+1.
        We can have more than one peaks but we can just return the first peak we encounter
        We have to return the index. If it's the first or last element of the array, we will or element is greater than the element outside the array. So we just check if the element is greater than previous element for the last element and for the frist one, we check if th element is greater than the next element
        M: 
        P: The problem is converting this to O(logn) times.
        We can do O(n) by doing a for loop:
        if n > n+1 and n> n-1:
            return n(it will be index)
        edge cases would be: we need to make sure it is not the first one or last element
        in that case we do if first value: check this. if last value check this: 
        that will be O(n)
        We can probably use a min heap to do this in O(log n)
        How to use min heap or maybe a bianry search. 
        """

        left = 0
        right = len(nums) -1 


        # why not left <= right
        while left < right:
            mid = (left+right)//2

            #If we are going uphill, we are guranteed to find a peak on the right

            if nums[mid] < nums[mid + 1]:
                #why not mid +1
                left = mid +1
            
            # why right = mid why not mid +1
            # discriminaion damn
            #if we are goign downlhill, we agre guranteed a peak there
            if nums[mid] > nums[mid + 1]:
                right = mid
        
        return left
            