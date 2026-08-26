class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        A brute force would be two nested loops that add every number once.
        An O(n) solution would be:
        1. We can have a dict of all the elements in nums
        2. then we can figure out by doing need = target - current
        3. if need is in target we return that index. so dict probably needs to store key, value.
        4. If 
        """

        seen = {}
        
        for index, number in enumerate(nums):
            need = target - number

            if need in seen:
                return [seen[need], index]
            
            seen[number] = index
