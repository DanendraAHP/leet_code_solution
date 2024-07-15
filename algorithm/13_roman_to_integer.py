"""

"""
import sys
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_CHAR = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        ROMAN_VAL = [1, 5, 10, 50, 100, 500, 1000]
        num = 0
        for char_idx, char in enumerate(s):
            if char_idx==len(s)-1:
                num+=ROMAN_VAL[ROMAN_CHAR.index(char)]
            else:
                if ROMAN_VAL[ROMAN_CHAR.index(char)] < ROMAN_VAL[ROMAN_CHAR.index(s[char_idx+1])]:
                    num-=ROMAN_VAL[ROMAN_CHAR.index(char)]
                else:
                    num+=ROMAN_VAL[ROMAN_CHAR.index(char)]
        return num

def main():
    # read the input
    txt = sys.argv[1]
    #invoke the solution
    s = Solution()
    n = s.romanToInt(txt)
    print(n)
if __name__=='__main__':
    main()