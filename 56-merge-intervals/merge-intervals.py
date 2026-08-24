class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        For an interval to overlap, the numbers inside the interval should fall withing it.
        So, the condition for an interval to overlap is:
            if  next_interval[0] < current_interval[1]:
                it overlaaps
        To ensure we can use this conditoon we can sort the intervals using the first value of the intervals.
            it will take O(n log n) time for sorting
        1. we sort the intervals by the frist value
        2. we keep a result array 
        3. we go through the sorted array, and see the current interval and the next interval
        4.     if  next_interval[0] < current_interval[1]:
                it overlaaps
        5. if it overlaps:
            6. we make the interval [current_interval[0], max(current_interval[1], next_interval[1])]
        7. if it does not overlap we append the interval to result tab

        """
        if not intervals:
            return []
        result = []

        intervals.sort(key=lambda interval: interval[0])

        current_interval = intervals[0]
        # We use -1 to make sure next_interval is not out of index
        for next_interval in intervals[1:]:
            if next_interval[0] <= current_interval[1]:
                        current_interval[1] = max(
                            current_interval[1],
                            next_interval[1]
                        )

            else:
                result.append(current_interval)
                current_interval = next_interval

        result.append(current_interval)
        return result