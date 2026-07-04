class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        1. Create a hashmap with vowels for O(1) lookup
        2. Fixed sliding window problem
        3. We start witha counter and check how many vowels in first window
        4. Then a for loop to update the count.
        5. For loop starts from k to len(s)
        """
        
        vowels = {"a", "e", "i", "o", "u"}
        window = s[:k]
        max_vowels = 0
        current_count = 0
        for i in window:
            if i in vowels:
                current_count +=1
        max_vowels = current_count
        for right in range(k, len(s)):
            if s[right] in vowels:
                current_count +=1
            
            if s[right-k] in vowels:
                current_count -=1
            
            max_vowels = max(max_vowels, current_count)

            if max_vowels == k:
                return k
        return max_vowels
