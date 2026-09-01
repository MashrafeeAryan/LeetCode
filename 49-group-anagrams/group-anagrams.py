class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        We will do a count that uses 
        A list where we use ord to keep frequnecy of each letter of key

        """ 

        groups ={}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c) - ord("a")] +=1

            key = tuple(count)

            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)


        return list(groups.values())
