# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        h=head
        l=[]
        while h:
            l.append(h.val)
            h=h.next
            
        n=len(l)//2
        i=0
        j=len(l)-1
        k=0
        while n>0:
            n-=1
            if (l[i]+l[j])>k:
                k=(l[i]+l[j])
            
            i+=1
            j-=1
            
        return  k   
            