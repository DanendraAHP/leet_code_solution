"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
import sys
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_distance = 10**4
        closest_sum = 0
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    sum_3 = nums[i]+nums[j]+nums[k]
                    distance = target - sum_3
                    if distance<=closest_distance:
                        closest_distance=distance
                        closest_sum = sum_3
        return closest_sum
    def threesumClosestOptimized(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_diff = 10**5
        closest_sum = 0
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            while start<end:
                sum_3 = nums[i]+nums[start]+nums[end]
                diff = abs(target-sum_3)
                if sum_3==target:
                    return sum_3
                elif diff<closest_diff:
                    closest_diff = diff
                    closest_sum = sum_3
                if sum_3>=target:
                    end-=1
                else:
                    start+=1
        return closest_sum

def main():
    # read the input
    nums, target = sys.argv[1], sys.argv[2]
    nums = nums.replace('[','').replace(']','')
    nums = nums.split(',')
    nums = [int(n) for n in nums]
    target = int(target)
    #invoke the solution
    s = Solution()
    n = s.threesumClosestOptimized(nums, target)
    print(n)
if __name__=='__main__':
    main()