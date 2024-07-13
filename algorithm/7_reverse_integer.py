"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
import sys
class Solution:
    def reverse(self, x: int) -> int:
        new_x = ''
        is_negative = x<0
        x = abs(x)
        while x//10>0:
            new_x+=str(x%10)
            x//=10
        new_x+=str(x)
        new_x = int(new_x)
        #check overflow
        if new_x>2**31-1 or new_x<-2**31:
            return 0
        return -1*new_x if is_negative else new_x
def main():
    # read the input
    num = sys.argv[1]
    #post-process input
    num = int(num)
    # invoke the solution function
    s = Solution()
    n = s.reverse(num)
    #n = s.longestPalindromeBruteForce(txt)
    print(n)
if __name__=="__main__":
    main()