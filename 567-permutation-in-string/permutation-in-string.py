class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        1. if s2> s1:
        2. Sliding window. fixed
        3. Define the first window which be s2[:len(s1)]
        4. Avoid slicing strings
        5. Keep a frequency count in dict where we can match the dict of the window and s1
        6. To remove and add to sliding window:
            1. we can reduce the count of the left most element in the window by 1
            2. we increase the count for the new addition to sliding window

        """

        if len(s1) > len(s2):
            return False
        
        k = len(s1)
        
        #S1 dict
        s1_freq = {}
        s2_freq ={}
        for i in s1:
            if i in s1_freq:
                s1_freq[i] +=1
            else:
                s1_freq[i] = 1
        
        for i in s2[:k]:
            if i in s2_freq:
                s2_freq[i] +=1
            else:
                s2_freq[i] =1

        if s1_freq == s2_freq:
            return True
        for right in range(k, len(s2)):
            if s2[right] in s2_freq:
                s2_freq[s2[right]] +=1
            else:
                s2_freq[s2[right]] = 1

            s2_freq[s2[right-k]] -=1

            if s2_freq[s2[right-k]] == 0:
                del s2_freq[s2[right-k]]
    
            if s1_freq == s2_freq:
                return True
        return False












