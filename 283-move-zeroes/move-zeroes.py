class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        1. Two Pointers
        2. read =0, write =0
        3. if read value != 0:
        4. nums[write] = nums[read] to replace the values
        5. nums[read]=0
        """

        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write+=1
        
        while write < len(nums):
            nums[write] = 0
            write+=1