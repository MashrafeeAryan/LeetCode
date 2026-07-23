class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1

        char = list(s)
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O","U"}
        while left < right:
            if char[left] not in vowels:
                left+=1
            
            elif char[right] not in vowels:
                right-=1
            else:
                temp = char[left]
                char[left] = char[right]
                char[right] = temp
                left+=1
                right-=1
            
        return "".join(char)