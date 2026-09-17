class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        U: We take the array and find how many len() longest sequence of consectuvie integers we have. If we have an arrya of [1,2,3,4,5,200]. We will say [1,2,3,4,5] is consecutive sequence and return 5 as len
        Conditions:
            - We need to do this in O(n) time
            - Rules out any sorting alogirthms including binary search
            - rules out min heap which has internal sorting and wont run in O9N)
        
        P: We would have used sliding window if it was sorted.  
        We can convert nums to a set to have O(1) look up. 
        When we are looping we say is there currentValue -1 in the set, if there is not
        then it is the start of a sequence most probably.
        Then we just keep adding one to the currentValue and check if it is in the set.
        If in the set, we increase the count by 1 to get the len
        We avoid checking the same sqeunce more thna one time by checkling if it is the start or not.

        Edge case:
        what if the start value is duplicated. We can avoid that by adding the start vlaues in a se and saying if not this start value.
        """

        maxLen = 0

        nums_set = set(nums)

        for num in nums_set:
            # if it is the start
            if not num -1 in nums_set:
                curr = num
                currLen = 1
                while curr + 1 in nums_set:
                    currLen+=1
                    curr+=1
                maxLen = max(maxLen, currLen)

        return maxLen
            