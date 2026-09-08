class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
            If it si a power of two, covert that number in binary it will only have 1 and all other values 0s

            and You can ensure if it has only one 1 by using bitwsie operator &. 

            So you can say n-1 = 0111 and n = 1000. so we can do n & (n-1)
            return n & (n-1) // true if power of two false if otherwise. now hwo do we deal with negative integers
        """
        if n<=0:
            return False
        
        return (n & n-1) == 0