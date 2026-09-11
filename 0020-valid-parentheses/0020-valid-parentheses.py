class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != valid[ch]:
                    return False
                stack.pop()

        return len(stack) == 0