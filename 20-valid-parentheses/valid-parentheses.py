class Solution:
    def isValid(self, s: str) -> bool:
        """
        Every closing brackets must match the most recent opening bracket
        1. We can create a dictionary where we have all the closing brackets associated with opening brackets
        2. We can do a siple O(n) serch in dictioanry to see if this closing bracket is in the dict,
        3. we check is it the closing bracket of the most recent opening bracket
        4. to keep track of most recent opening bracket we use a stack

        """

        stack = []

        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s:
            if i in "({[":
                stack.append(i)
            
            else:
                if not stack:
                    return False
                
                if stack[-1] != pairs[i]:
                    return False
                
                stack.pop()

        return len(stack) == 0
                
            