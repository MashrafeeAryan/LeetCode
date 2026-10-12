class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        U: We are efinding the length of last word of the string adn returning it
        M:
        P:
        We will have a loop and a stack called length
        loop through each character:
        3. when encounter a letter add to length
        4. when encounter a space make add the length to the stack and make length 0
        5. return the end value of the stack
        I:
        R:
        E: O(n)
        O(N) space and time comelxity
        """

        size = []
        len = 0


        for st in s:
            if st.isalnum():
                len+=1
            else:
                if len>0:
                    size.append(len)
                    len = 0
        
        if len>0:
            size.append(len)
        
        return size[-1]