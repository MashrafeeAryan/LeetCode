class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        We can't ise dicct as keus becuase these are not immutable
        So we can do somethng where we have groups dict
        We loop through every word and create a index list with 26 characters
        We take every chacter and find it's corresponding index using ord("char") - ("ä")
        we conver the list to a tuple and add it to dict
        
        """
        group = {}

        for word in strs:
            char = [0] * 26

            for i in word:
                char[ord(i) - ord("a")] +=1
                
            
            key = tuple(char)

            if key not in group:
                group[key] = []
            
            group[key].append(word)

        return list(group.values())