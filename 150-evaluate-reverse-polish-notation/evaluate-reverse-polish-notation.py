class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        We keep the numbers inside the stack and pop hem after we did our calculations
        so if not one of the four openrads it gets appended. 
        when it encouters an operand it will use that operance 

        """

        stack = []

        operands = {'+', '-', '*', '/'}
        for i  in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                if i == '+':
                    result = left + right
                elif i == "-":
                    result = left -right
                elif i == "*":
                    result = left * right
                else:
                    result = int(left/right)
                
                stack.append(result)
        
        return stack[-1]