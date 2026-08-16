class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        We are just implementign a sorting algorithm
        """

        """
        Since we know there are only three possible values
        1. We can make a dictionary of the frequency of 0,1,2
        2. We can use the number of frequencies and loop through nums and keep replacing in place.
        """
        from collections import Counter

        freq = Counter(nums)

        count_index =0
        for i in range(3):
            j = 0
            while j < freq[i]:
                nums[count_index] = i
                count_index+=1
                j+=1
        