class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        sign = 1
        number = 0

        # 1. Skip leading spaces.
        while index < len(s) and s[index] == " ":
            index += 1

        # 2. Read one optional sign.
        if index < len(s) and s[index] == "-":
            sign = -1
            index += 1
        elif index < len(s) and s[index] == "+":
            index += 1

        # 3. Read digits.
        while index < len(s) and s[index].isdigit():
            digit = ord(s[index]) - ord("0")
            number = number * 10 + digit
            index+=1

        number = number * sign

        # 5. Clamp to 32-bit signed integer range.
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if number < INT_MIN:
            return INT_MIN

        if number > INT_MAX:
            return INT_MAX

        return number