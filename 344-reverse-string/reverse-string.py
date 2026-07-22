class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Use two pointers
        1. left pointer at index 0
        2. Right pointer at len(s)-1
        3. We swtich the element of left pointer with element of right pointer
        4. then move them
        5. while left < right, we keep doing it
        """

        l = 0
        r = len(s)-1

        while l < r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l+=1
            r-=1
        