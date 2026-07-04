class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Variable Sliding Window
        1. We can keep a frequency of characters in our window
        2. we just increase the size of window till we encounter a duplicate character.
        3. we reduce the size fo window from left till we no logner have duplciate character in our window.
        4. we keep track of bggest window using max
        """
        left = 0
        longest = 0
        seen = set()
        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            longest = max(longest, right-left+1)
        return longest