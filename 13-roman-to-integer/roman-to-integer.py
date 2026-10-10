class Solution:
    def romanToInt(self, s: str) -> int:
        """
        U: need to convert the roman numerals into integers
        M: 
        P:
        I, V, X, L, C, D, M

        However, if I is followed by V and X it is different
        X is followed by L, and C 
        C follwed by D and M

        1. We loop through s:
        2. If s is I, X or C we check is it followed by their respective alphabets relaed to them like I followed by V or X
        3. If that is the case we check for the corresponding value in dict and add it to our result
        4. if not the case we find corresponding value of I and add to result
        """

        result  = 0

        numeral_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        index = 0

        while index < len(s):
            if s[index] in "IXC" and index != len(s)-1:
                temp = s[index] + s[index+1]
                if temp in numeral_dict:
                    result += numeral_dict[temp]
                    index+=2
                else:
                    result+= numeral_dict[s[index]]
                    index+=1
            else:
                result += numeral_dict[s[index]]
                index+=1
        
        return result
                