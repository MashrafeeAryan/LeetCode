class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        """
        1. We process groups here
        2 So we have start and end pointers
        3. a while loop that goes through eveyr group with condition as long as start < len(s)
        4. another while loop that finds the end of a particular group. So the condition might be as long as the current character is same as first element of the group we keep adding one to end. to find the end of the group
        5. Then, we process it. We do a length count end - start. We get the length of the group
        6. if the group length is > 3, we append [start, end] to interval list
        7. after the first while loop ends , we return the interval list
        """
        start = 0
        n = len(s)
        interval = []

        while start < n:
            end = start # to move the end index to the start of next group

            while end < n and s[end] == s[start]:
                end+=1
            

            length = end - start

            if length >= 3:
                interval.append([start, end-1])
            
            start = end
        return interval