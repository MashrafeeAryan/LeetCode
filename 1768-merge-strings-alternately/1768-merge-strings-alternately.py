class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        U:  We are merging the string my alternatively adding letters from the string
        M:
        P: 
        1. list to store the alternate letters
        2. left = index of word1, right = indexof word2
        2. 
        I:
        R:
        E:
        """

        left = 0
        right = 0
        leth = []
        while left < len(word1) and right < len(word2):
            leth.append(word1[left])
            leth.append(word2[right])
            left +=1
            right+=1
        
        if len(word2) > len(word1):
            while right < len(word2):
                leth.append(word2[right])
                right+=1
        else:
            while left < len(word1):
                leth.append(word1[left])
                left+=1
        
        return "".join(leth)