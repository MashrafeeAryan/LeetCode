class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarray_no = 0
        prefix_sum = 0
        freq_counter = {0: 1}

        for num in nums:
            prefix_sum += num
            val = prefix_sum - k

            subarray_no += freq_counter.get(val, 0)

            freq_counter[prefix_sum] = (
                freq_counter.get(prefix_sum, 0) + 1
            )

        return subarray_no