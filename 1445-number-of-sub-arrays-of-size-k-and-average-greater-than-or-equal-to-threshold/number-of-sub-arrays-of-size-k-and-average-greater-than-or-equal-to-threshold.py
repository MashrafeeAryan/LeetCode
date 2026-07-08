class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
            Goal: return the NUMBER of subarrays that has average greater than or equal to threshold
            So return the number of windows that has that average.
            We do not need to store subarrays, we can just count how many times a window's average crosses threshold.
            1. initialize the fist window
            2. Calculate the sum
            3. Check if it crosses the threshold. If it does, increase count of no_of_subarrays by one
            4. create a for loop for sliding window starting from (k, len(arr)):
            5. we add right most element of the window to the sum
            6. We remove left most element of the window or subtract

        """

        window_sum = sum(arr[:k]) # We can do this or for loop
        average = window_sum/k

        no_of_subarrays = 0

        if average >= threshold:
            no_of_subarrays+=1
        

        for right in range(k, len(arr)):
            window_sum+= arr[right]
            window_sum -= arr[right-k]
            average = window_sum/k
            if average >= threshold:
                no_of_subarrays+=1
        
        return no_of_subarrays