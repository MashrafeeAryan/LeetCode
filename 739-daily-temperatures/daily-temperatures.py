class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """"
        We have a stack
        and resutl array
        1. We loop through temperatures
        2. We append the first value if stack is empty
        3. We then keep adding if we do not find a temp higher.4. is 74>32 oh yes
        4. we remove 73 and say distance one and add 74
        5. is 
        """

        stack = []
        result = [0] *len(temperatures) 
        for current_index  in range(len(temperatures)):
            while stack and temperatures[current_index ] > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = current_index - previous_index

            stack.append(current_index)
        return result