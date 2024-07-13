"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
import sys
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x)//2):
            if x[i]!=x[len(x)-i-1]:
                return False
        return True
    def isPalindromeINT(self, x:int) -> bool:
        if x<0:
            return False
        temp_x  = x
        reversed_x = 0
        while temp_x!=0:
            last_digit = temp_x%10
            reversed_x = reversed_x*10+last_digit
            temp_x//=10
        return reversed_x==x
def main():
    # read the input
    n = sys.argv[1]
    #post process input
    n=int(n)
    #invoke the solution
    s = Solution()
    n = s.isPalindromeINT(n)
    print(n)
if __name__=='__main__':
    main()