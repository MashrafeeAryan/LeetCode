import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        U: We will return the kth largest element in array. So if k is 2, we return second largest element in an array
        Conditions: 
            - Sorting not allowed: rules out binary, sort()
            - Not distinct element. So, if k=2, and both the largest and second largest number is 5, we chose 5
            - if len(nums) > k
        
        I: 
            We can use a min heap where the smallest one will be at the top.
            To get the second largest one: we probably need to pop len(nums) -k times?
            BUt min heap does sort internally.
            To only have k values instead of n values in our heap, we can probably pop out the min values if the heap size is greater than k. as a result our answer will always be index -0 of the min heap

        """

        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
            

        
        return heapq.heappop(heap)