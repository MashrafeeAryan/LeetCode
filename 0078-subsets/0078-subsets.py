class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        U: We need to return all possible cominations of three nums including all possible combination of nums including the combinations of each elements of nums.
        M: Seems like we are trying different things so recursiong Dfs and backtracking would help
        P: How does dfs template look like
        """

        result = []
        current = []
        
        def dfs(index):

            #Base case:
            if index == len(nums):
                #We append copy neause if we drectly append current, ti appends the reference to current as well so when we pop it it removes it form reuslt as well which we do not want
                result.append(current.copy())
                return 
            
            #Explore:
            current.append(nums[index])
            #Move on
            dfs(index+1)

            #Pop() or exclude
            current.pop()

            #Exclude:
            dfs(index+1)

        
        dfs(0)
        return result