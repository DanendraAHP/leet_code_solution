"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List
import sys
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return i,j
def main():
    # read the input
    nums, target = sys.argv[1], sys.argv[2]
    # post-process the input
    nums = nums.replace('[','').replace(']','')
    nums = nums.split(',')
    nums = [int(n) for n in nums]
    target = int(target)
    # invoke the solution function
    s = Solution()
    i,j = s.twoSum(nums, target)
    print([i,j])
if __name__=="__main__":
    main()