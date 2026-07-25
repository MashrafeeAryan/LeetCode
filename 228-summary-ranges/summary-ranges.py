class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        1. We have a start at 0. We are trying to group them
        2. We set a while condition to go through the array while start is less than the length of nums
        3. We set end = start so both move together when new group starts.
        4. another while loop to find groups. So, while end < len(nums) and nums[end] == nums[end-1]+1
        5. we didn't account for first element in our condition
        6. if the condition meets, we 
        """
        start = 0
        n = len(nums)

        result = []
        while start < n:
            end = start

            while end + 1 < n and nums[end + 1] == nums[end]+1:
                end+=1
            
            if start == end:
                result.append(f"{nums[start]}")

            else:
                result.append(f"{nums[start]}->{nums[end]}")

            start = end+1
        return result