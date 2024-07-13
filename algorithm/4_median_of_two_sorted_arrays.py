"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
import sys
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined_length = len(nums1)+len(nums2)
        sorted_nums = []
        nums1_idx = 0
        nums2_idx = 0
        for i in range(combined_length//2+1):
            num1_val = nums1[nums1_idx] if nums1_idx<len(nums1) else 1000000
            num2_val = nums2[nums2_idx] if nums2_idx<len(nums2) else 1000000
            if num1_val < num2_val:
                appended_val = num1_val
                nums1_idx+=1
            else:
                appended_val = num2_val
                nums2_idx+=1
            sorted_nums.append(appended_val)
        if combined_length%2==0:
            return sum(sorted_nums[-2:])/2
        else:
            return sorted_nums[-1]


def main():
    # read the input
    nums1, nums2 = sys.argv[1], sys.argv[2]
    # post-process the input
    nums1 = nums1.replace('[','').replace(']','')
    nums1 = nums1.split(',')
    nums1 = [int(n) for n in nums1]
    nums2 = nums2.replace('[','').replace(']','')
    nums2 = nums2.split(',')
    nums2 = [int(n) for n in nums2]
    # invoke the solution function
    s = Solution()
    n = s.findMedianSortedArrays(nums1, nums2)
    print(n)
if __name__=="__main__":
    main()