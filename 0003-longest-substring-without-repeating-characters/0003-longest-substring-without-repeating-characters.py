class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We use a pointers and a window
        Our It starts from the first index and second letter
        We loop through the string and then have a while loop for the whindow.
        when we encounter a chacter that is already in our window we keep reducing th ewindow size from left till the chavracter is no longer in our window
        """

        left = 0
        maxVal = 0
        seen = set()
        if not s:
            return 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            maxVal = max(maxVal, right - left +1)
        
        return maxVal