class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. We can loop through the array
        2. Use counter to create a frequency of characters in each word
        3. We use that frequency and convert it into tupple to use as a key
        4. An anagram should have the same frequency so we use that as a key and if anagram has same key we just append it to the dict
        5. We return a list of values 
        """
        from collections import Counter, defaultdict
        
        group = defaultdict(list)
        for word in strs:

            freq = Counter(word)

            key = tuple(sorted(freq.items()))

            group[key].append(word)

        return list(group.values())
