from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        U: We have to figure out if s is a good string or bad string. If all elements in s appear same number of times, it is a good string. Otherwise abd string. good string is saame frequency for the elements.
        M: hash? counter?
        P: One option: Use Counter() and just check if the frequency is the same using a for loop
        it will coontain atleast one letter
        """
        
        s_freq = Counter(s)
        occurence  = s_freq[s[0]]
        for value, freq in s_freq.items():
            if freq != occurence:
                return False
        
        return True
            