import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        the brute force method would be loop through the list get the distance between origin and the coordinate append it to result or min heap.
        we can then pop as many times as k is without sorting it again but if min heap and sort ahve equal O(nlogn) time complexity we rather sort it. 
        """

        heap = []

        for coord in points:
            distance = coord[0]**2 + coord[1]**2
            heapq.heappush(heap, (distance, coord[0], coord[1]))
        

        result = []
        while k:
            coord = [0,0]
            distance, coord[0], coord[1] = heapq.heappop(heap)

            result.append(coord)
            k-=1
        
        return result