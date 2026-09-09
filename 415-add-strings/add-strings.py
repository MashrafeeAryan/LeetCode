class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        The while loop condition should be somethiing that lets it run till both gets done

        """
        i = len(num1) - 1
        j = len(num2)-1
        carry = 0
        result = []
        while i >= 0 or j >=0 or carry > 0:
            
            if i >=0:
                digit1 = ord(num1[i]) - ord("0")
            else:
                digit1 = 0

            if j>=0:
                digit2 = ord(num2[j]) - ord("0")
            else:
                digit2 = 0
            
            total = digit1 + digit2 + carry
            
            digit = total % 10
            carry = total//10
            result.append(str(digit))
            i-=1
            j-=1
        return "".join(result[::-1])