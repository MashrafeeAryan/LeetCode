class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        U: We need to find the words in the word dict in s. If we find all the words, return true or elese false. Note: words in s cannot have overlapping chacracters/ Look at example 3. all of the words techncall exist buyt if you use cats, you cant make cat. if you use sand you cant make dog.
        M:
        P:


        """

        memo = {}
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for word in wordDict:
                if s.startswith(word, start):
                    if dfs(start+len(word)):
                        memo[start] = True
                        return True
            
            memo[start] = False
            return False
            
        return dfs(0)