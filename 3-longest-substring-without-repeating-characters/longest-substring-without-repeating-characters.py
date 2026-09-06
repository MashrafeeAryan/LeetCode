class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We have a window where we keep adding letters and we can use a set for it.
        When we encounter a duplicate, we keep removing from the left side until the duplicteis not there anymore 
        """
        if not s:
            return 0
        substring = set()

        left = 0
        substring.add(s[left])
        maxSub = len(substring)
        for right in range(1, len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            
            substring.add(s[right])
            maxSub = max(maxSub, len(substring))
        
        return maxSub