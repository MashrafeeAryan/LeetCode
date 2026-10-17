class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        U: find the longest subsrting without duplicate characters
        M: set
        P:
        create a set and see if it is in there, 
        both space and time complextiy are O(n)
        can we optimize it further are without space

        """
        length = 0
        left = 0
        freq = set()
        for right in range(len(s)):
            while s[right] in freq:
                freq.remove(s[left])
                left+=1
            
            freq.add(s[right])
            length = max(length, right - left + 1)

        return length