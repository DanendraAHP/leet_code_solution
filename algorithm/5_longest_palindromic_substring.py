"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

import sys

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def check_palindrome(left, right):
            #expand the palindrom around its center
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        longest_palindrome = s[0]
        for i in range(len(s)):
            odd = check_palindrome(i,i)
            even = check_palindrome(i,i+1)
            if len(odd)>len(longest_palindrome):
                longest_palindrome = odd
            if len(even)>len(longest_palindrome):
                longest_palindrome = even
        return longest_palindrome
    def longestPalindromeBruteForce(self, s:str) -> str:
        if len(s)<=1:
            return s
        def check_palindrome(substring):
            for i in range(len(substring)//2):
                if substring[i]!=substring[len(substring)-1-i]:
                    return False
            return True
        longest_palindrome = s[0]
        for i in range(len(s)-1):
            for j in range(i, len(s)):
                if check_palindrome(s[i:j+1]):
                    if len(s[i:j+1])>len(longest_palindrome):
                        longest_palindrome =  s[i:j+1]
        return longest_palindrome
def main():
    # read the input
    txt = sys.argv[1]
    # invoke the solution function
    s = Solution()
    n = s.longestPalindrome(txt)
    #n = s.longestPalindromeBruteForce(txt)
    print(n)
if __name__=="__main__":
    main()