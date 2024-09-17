"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""
import sys
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i, len(height)):
                width = j-i
                min_height = height[i] if height[i]<height[j] else height[j]
                area = width*min_height
                if area>max_area:
                    max_area=area
        return max_area
    def maxAreaOptimized(self, height:List[int]) -> int:
        max_area = 0
        left_idx = 0
        right_idx = len(height)-1
        while left_idx<right_idx:
            width = right_idx-left_idx
            min_height = height[left_idx] if height[left_idx]<height[right_idx] else height[right_idx]
            area = width*min_height
            max_area = area if area>max_area else max_area
            if height[left_idx]<height[right_idx]:
                left_idx+=1
            else:
                right_idx-=1
        return max_area

def main():
    # read the input
    height = sys.argv[1]
    #post-process input
    height = height.replace('[','').replace(']','')
    height = height.split(',')
    height = [int(n) for n in height]
    #invoke the solution
    s = Solution()
    n = s.maxAreaOptimized(height)
    print(n)
if __name__=='__main__':
    main()