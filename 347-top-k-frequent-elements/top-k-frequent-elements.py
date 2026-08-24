from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Just make a dictioanry out of it that is jjust O(n) operation. in the dictionary it will be hard to get the most frequent k elements
        """

        """
        1. Make a dictionary at first
        2. We make empty buckets
        3. put each number in a bucket
        5. give last k numbers
        """

        freq = Counter(nums)

        freq_bucket = []

        for _ in range(len(nums) + 1):
            freq_bucket.append([])

        for number, frequency in freq.items():
            freq_bucket[frequency].append(number)

        result = []
        for freq in range(len(freq_bucket) - 1, 0, -1):
            for number in freq_bucket[freq]:
                result.append(number)

                if len(result) == k:
                    return result

        return result