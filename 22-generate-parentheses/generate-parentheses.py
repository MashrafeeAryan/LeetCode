class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        open < n:
        current.append("(")
        close < open

        """

        current = []
        result = []
        
        def backtrack(current, open, close):
            if open == n and close ==n:
                result.append("".join(current))
            if open < n:
                current.append("(")
                backtrack(current, open + 1, close)
                current.pop()
            
            if close < open:
                current.append(")")
                backtrack(current, open, close+1)
                current.pop()
            
        backtrack(current, 0, 0)
        return result