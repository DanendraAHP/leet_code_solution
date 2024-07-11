"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        longest_l = max(len(l1), len(l2))
        added_l = []
        temp_next = 0
        for i in range(longest_l):
            l1_val = 
            added_val = l1[i].val + l2[i].val + temp_next
            temp_val = added_val%10
            temp_next = added_val//10
            temp_ln = ListNode()
        #check which list is the longest
        l_diff = abs(len(l1)-len(l2))
        added_l = [0 for i in range(l_diff)]
        if len(l1)>len(l2):
            pass
def convert_to_listnode(l):
    lns=[]
    for i in range(len(l)):
        if i==len(l)-1:
            ln = ListNode(l[i],None)
        else:
            ln = ListNode(l[i],l[i+1])
        lns.append(ln)
    return lns
def main():
    # read the input
    l1, l2 = sys.argv[1], sys.argv[2]
    # post-process the input
    l1 = l1.replace('[','').replace(']','')
    l1 = l1.split(',')
    l1 = [int(n) for n in l1]
    l2 = l2.replace('[','').replace(']','')
    l2 = l2.split(',')
    l2 = [int(n) for n in l2]
    #convert list to ListNode
    l1 = convert_to_listnode(l1)
    l2 = convert_to_listnode(l2)
    print(l1[2], l2[2])
if __name__=="__main__":
    main()