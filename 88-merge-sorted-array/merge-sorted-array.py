"""
U: We have two sorted arrays and we have to merge it. To merge it we merge nums2 to nums1. So, we will merge it in place.
M: We will use two pointers
P: If we use two pointers from the m-1 for nums1 and from n-1 for nums2, we can compare which one is greater. The greater number goes to the end of nums1. 
I:
    1. One left and one right pointer
    2. Keep one at nums1 m-1 index. One pointer at nums2 n-1 index.
    3. Compare it. Whicver is greater append to len(nums1)-1 or replace it actually
    4. Move the pointer in the array which one you just added to nums1
    5. Problem: nums1 should always be greater than nums 2 otherwise just return []
        What condition do we use to make sure two pointers work or stop
        While nums2 is stll there. by the time we are done going through nums 2. it should be order.

"""
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = m-1
        right = n-1

        write = m + n - 1
        while right>=0:
            if left>=0 and nums1[left]>= nums2[right]:
                nums1[write] = nums1[left]
                left -=1
            else:
                nums1[write] = nums2[right]
                right-=1

            write-=1
        
        #In the case that nums 1 ends faster than nums2 we cna add nums2 to nums 1
        