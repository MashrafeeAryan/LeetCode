class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        U: We have an array of candies amount. We have to add 3 to each person's candies in an array. After adding, if that person has highest number of candies, we append true to the list
        M:
        P:
        The brute force method:
        One possible way would be to add extra cadide and check if it is greater than remaining one
        More optimized version might be go through candies one and create max stack.
        It will hold coressponding index and candies amount.
        1. maxindex (opposite of minheap) I forgot how to implemenet max index
        2. We have a variable result = []
        3. we loop through cnadies once and make a max heap
        3. loop through for i in range(candies):
        4.

        """

        largest_value = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= largest_value:
                result.append(True)
            else:
                result.append(False)
        
        return result