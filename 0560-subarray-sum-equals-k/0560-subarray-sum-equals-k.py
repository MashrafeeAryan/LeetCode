class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        prefix_count = {0: 1}

        for num in nums:
            # Add current number to running sum
            prefix += num

            # Check how many previous prefixes
            # would create a subarray with sum k
            if prefix - k in prefix_count:
                count += prefix_count[prefix - k]

            # Store the current prefix for the future
            prefix_count[prefix] = prefix_count.get(prefix, 0) + 1

        return count