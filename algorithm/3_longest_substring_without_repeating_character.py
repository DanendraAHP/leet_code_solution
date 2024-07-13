"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
import sys

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)>1:
            max_len=0
            for i in range(len(s)-1):
                for j in range(i+1, len(s)+1):
                    if len(s[i:j])==len(set(s[i:j])):
                        length = j-i
                        if length>max_len:
                            max_len = length
        else:
            max_len = len(s)
        return max_len


def main():
    # read the input
    txt = sys.argv[1]
    # invoke the solution function
    s = Solution()
    n = s.lengthOfLongestSubstring(txt)
    print(n)
if __name__=="__main__":
    main()
