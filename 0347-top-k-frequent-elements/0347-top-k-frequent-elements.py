from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        1. We would have a counter function and get the frequencies of all the numbers
        2. We can use the frequnceis as indexes and keys of counter fucntions as valuees.
        3. Then we can loop from the end of the list to the get the top k freqincies. Because if index is frequency the end frequcny should be part of top k
        """
        # Frequnecy of nums
        freq_dict = Counter(nums)


        #We are trying to convert frequecies as index and keys as values
        #freq not > len(nums)
        values = []
        #Same number can have same frequncy and we want to store them together.
        #for that we need them in a []
        for _ in range(len(nums)+1):
            values.append([])

        for key, freq in freq_dict.items():
            values[freq].append(key)
        result = []
        for i in range(len(values)-1, 0, -1):

            for num in values[i]:
                result.append(num)

            if len(result) == k:
                return result
        return []