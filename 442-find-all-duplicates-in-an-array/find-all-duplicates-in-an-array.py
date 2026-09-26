class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        """
        u: At most integers will appear twice. All positive numbers. We are returning an array of integeters that appear twice. 
        M:
        P: Can we use a set to store or since it's onstant auuxiliary space we can't do that.
        """

        result = []

        for i in range(len(nums)):
            #Get original
            value = abs(nums[i])

            index = value -1

            if nums[index] < 0:
                result.append(value)
            
            else:
                nums[index] = -nums[index]
        
        return result