class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ 
        We use two pointers 
        1. Define one pointer at the start 
        2. Right pointer = len(s) - 1
        3. s_new = s.strip()
        3. while left < right:
        4. if s_new[left].isalnum():
            left +=1
        5. if s_new[right].isalnum():
            right+=1
        6. if s_new[left].lower() != s_new[right].lower()
        5. false
        7. At thend of while loop, outside while loop return true
        """
        left = 0
        right = len(s)-1
    
        while left < right:
            while left< right and s[left].isalnum() == False:
                left +=1
            while left < right and s[right].isalnum() == False:
                right -=1

            if s[left].lower() != s[right].lower():
                return False

            left+=1
            right-=1
        return True