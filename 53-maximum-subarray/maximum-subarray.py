class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        We can probably use a window where we add right elemtn to window.
        if it makes it greater tha previou one we keep it. if it makes it less we just remove the left element.

        """

        current_sum = nums[0]
        best_sum = nums[0]

        for number in nums[1:]:
            # Is it better to just start from this number or use previous subarray
            current_sum = max(number, current_sum + number)

            best_sum = max(best_sum, current_sum)

        return best_sum