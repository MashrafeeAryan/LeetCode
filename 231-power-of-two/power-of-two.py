class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        For it to be power of two the binary should always look like: 0001, 1000, 0100 or with just one 1. 
        So we are just checking if the binary of the number has only 1
            1. and doing n+1 will result in 1110 or with just one 0 if it is power of 10.
            2. So we can & (AND) if both are ones it will be true or if both are zero
            3. n -1 will give 0111 So whn you do AND it becomes 0000 or 0 so we juist check that

        """
        return n > 0 and (n & (n-1) == 0)