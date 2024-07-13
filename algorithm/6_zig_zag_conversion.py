"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
import sys

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #initialized empty list
        l = ['' for _ in range(numRows)]
        #iterate
        row_end_idx = numRows-1
        s_idx = 0
        while s_idx<len(s):
            row_end_idx = row_end_idx if row_end_idx>0 else numRows-1

            if row_end_idx==numRows-1:
                row_idx = 0
                while row_idx<numRows and s_idx<len(s):
                    l[row_idx] += s[s_idx]
                    s_idx+=1
                    row_idx+=1
                    
            else:
                l[row_end_idx] += s[s_idx]
                s_idx+=1
                
            row_end_idx-=1
        return "".join(l)
        
def main():
    # read the input
    txt,row = sys.argv[1], sys.argv[2]
    #post-process input
    row = int(row)
    # invoke the solution function
    s = Solution()
    n = s.convert(txt, row)
    #n = s.longestPalindromeBruteForce(txt)
    print(n)
if __name__=="__main__":
    main()