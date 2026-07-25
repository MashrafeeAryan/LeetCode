class Solution:
    def maxPower(self, s: str) -> int:
        write = 0
        start = 0
        n = len(s)
        maxCount = 0
        while start < n:
            end = start

            while end < n and s[end]  == s[start]:
                end+=1

            count = end - start
            maxCount = max(count, maxCount)

            start = end
        

        return maxCount