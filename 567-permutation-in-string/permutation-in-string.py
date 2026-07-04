class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        k = len(s1)
        s1_freq = {}
        for i in s1:
            if i in s1_freq:
                s1_freq[i] +=1
            else:
                s1_freq[i] = 1
  
        s2_freq = {}
        for i in range(k):
            if s2[i] in s2_freq:
                s2_freq[s2[i]] +=1
            else:
                s2_freq[s2[i]] = 1
        
        if s1_freq == s2_freq:
            return True

        for right in range(k, len(s2)):
            if s2[right] in s2_freq:
                s2_freq[s2[right]] +=1
            else:
                s2_freq[s2[right]] = 1
            
            if s2[right-k] in s2_freq:
                s2_freq[s2[right - k]]-=1

            if s2_freq[s2[right-k]] ==0:
                del s2_freq[s2[right-k]]
            if s2_freq == s1_freq:
                return True
        return False