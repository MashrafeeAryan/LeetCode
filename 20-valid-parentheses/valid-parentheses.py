class Solution:
    def isValid(self, s: str) -> bool:
        """
        1. A while loop, if it is an opening bracket push it.
        2. 

        """

        stack = []
        parentheses_dict = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for i in range(len(s)):
            if s[i] not in parentheses_dict:
                stack.append(s[i])
            else:
                if not stack or stack[-1] != parentheses_dict[s[i]]:
                    return False

                stack.pop()
        
        return not stack