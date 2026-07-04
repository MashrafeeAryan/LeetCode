class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Fixed variable sliding problem
        len(p) < len(s)
        return []

        1. Get the length of p
        2, Create a freq counter for p
        3. Create a fre counter for s[:k]
        4. Compare both
        5. Move the window
            6 . Add another element
            7. Remove leftmsot element (right-k)
        """
        if len(p) > len(s):
            return []
        index_array = []
        p_freq ={}
        k = len(p)
        for i in p:
            if i in p_freq:
                p_freq[i] +=1
            else:
                p_freq[i]=1
        
        s_freq = {}

        for i in s[:k]:
            if i in s_freq:
                s_freq[i]+=1
            else:
                s_freq[i] =1

        if s_freq == p_freq:
            index_array.append(0)
        
        for right in range(k, len(s)):
            if s[right] in s_freq:
                s_freq[s[right]]+=1
            else:
                s_freq[s[right]]=1
        
            if s[right - k] in s_freq:
                s_freq[s[right-k]]-=1
                
            if s_freq[s[right-k]] ==0:
                del s_freq[s[right-k]]
            
            if s_freq ==p_freq:
                index_array.append(right-k+1)
        
        return index_array