"""

"""
import sys
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(s) for s in strs])
        prefix=""
        for i in range(min_len):
            current_char = strs[0][i]
            for s in strs:
                if current_char!=s[i]:
                    return prefix
            prefix+=strs[0][i]
        return prefix

def main():
    # read the input
    strs = sys.argv[1]
    strs = strs.replace('[','').replace(']','')
    strs = strs.split(',')
    #invoke the solution
    s = Solution()
    n = s.longestCommonPrefix(strs)
    print(n)
if __name__=='__main__':
    main()