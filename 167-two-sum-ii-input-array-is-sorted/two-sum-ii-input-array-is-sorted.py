class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        1. Have a pointer at left and a pointer at right
        2. Add them up to see if they match target
        3. If sum lower than target, move the left pointer it will increase the sum
        4. If sum greater than target, move the right pointer it will decrease thes um
        5. We are guranteed a solution if we use two pointers in O(n)

        """
        left = 0
        right = len(numbers)-1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum < target:
                left+=1
            elif current_sum > target:
                right -=1
            else:
                return [left+1, right+1]
    