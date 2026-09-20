class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        """
        U: We are guranteed that our list will have "++X", "X++", "--X", "X--" So, everytime we encounter -- or ++ we have to add -1 or +1 to X=0.
        M: We probalby need to check if + or i is in the string which will be O(3).
        P: 1. Loop through the operations.
            2. if + in str: then add one
            3. if - in str: then subtract one
            4. It will alwas have + or -


        """

        x = 0

        for stri in operations:
            if "+" in stri:
                x+=1
            else:
                x-=1
        
        return x