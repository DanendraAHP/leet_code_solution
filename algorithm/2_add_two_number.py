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
class LeetCodeSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_ln = ListNode()
        last_node = new_ln
        next_val = 0

        while l1 is not None or l2 is not None or next_val!=0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            sum_val = val1+val2+next_val
            val = sum_val%10
            next_val = sum_val//10
            new_node = ListNode(val)
            last_node.next = new_node
            last_node = last_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        result = new_ln.next
        new_ln.next = None
        return result
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        longest_l = max(len(l1), len(l2))
        added_l = []
        temp_next = 0
        for i in range(longest_l):
            try:
                l1_val = l1[i].val
            except:
                l1_val = 0
            try:
                l2_val = l2[i].val
            except:
                l2_val = 0
            added_val = l1_val+l2_val + temp_next
            temp_val = added_val if added_val<10 else added_val-10
            temp_next = added_val//10
            temp_ln = ListNode(temp_val, None)
            added_l.append(temp_ln)
            if i>0:
                added_l[i-1].next = temp_val
        #last added
        if temp_next>0:
            added_l.append(ListNode(temp_next, None))
            added_l[len(added_l)-2].next = temp_next
        return added_l
    
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
    #invoke solution
    s = Solution()
    added_l = s.addTwoNumbers(l1, l2)
    print([l.val for l in added_l])
if __name__=="__main__":
    main()