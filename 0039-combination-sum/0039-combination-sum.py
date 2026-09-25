class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """ 
        U: We have to return a list of unique combinations of integers that add up to our target.
        M:
        P: We are trying out various things and moving back if it doesnt work. So a dfs and back tracking. What we can do is. if current element doesnt add up to target we go to next element - does it add up/ nope move to next but htat ebcomes tw for loops help bro
        """

        result = []
        def dfs(current, remaining, i):
            if remaining == 0:
                result.append(current.copy())
                return
            

            if i == len(candidates):
                return
            
            #We have to skip
            if remaining < 0:
                return

            #Take
            current.append(candidates[i])
            dfs(current, remaining - candidates[i], i)
            current.pop()


            dfs(current, remaining, i+1)

        dfs([], target, 0)
        return result
