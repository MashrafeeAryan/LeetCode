class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        1. we group each of the letters and see if they have three or more consecutive letters,
        2. If they do we take those out.
        3. start = 0
        4. write = 0
        5. we use a while loop that loops through the whole string wiht condition start < len(s)
        6. end = start to reinitialize the end to another group
        7. another while loop to find the group end. So, when s[end] == s[start]
        8. we process it
        9. length = [end - start]
        10. if length >= 3:
        11. How do i remove.
        12 
        """

        start = 0
        n = len(s)
        result = []
        while start < n:

            end = start

            while end < n and s[end] == s[start]:
                end+=1
            

            length = end - start
            keep = min(2, length)

            for _ in range(keep):
                result.append(s[start])
            
            start = end
        
        return "".join(result)