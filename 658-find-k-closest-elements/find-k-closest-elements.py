import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        U: We are given a sorted array and two integers k and x. We have to find the closest k number of integers to x. For instance, find 5 closest integers to x in the array
        M:
        P: 
            We do need to check every number because it is sorted. 
            The brute force method would be:
            1. loop through all numbers
            2. do x - curr: store it in a min heap with the arr[i] value
            2. store all in a min heap
            3. pop min hea 4 times
            4. append it into result: will give same thing

        However, since we do not ned to check every element, i wonder if binary search might help
        """
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left+right)//2

            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
            
        
        return arr[left:left+k]