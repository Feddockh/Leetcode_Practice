# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):

        # Create linked list head and current point for output
        head = point = ListNode(0)

        # Find number of linked lists
        k = len(lists)

        # Begin loop
        i = 0
        while (i < k):

            # Move to the next available list
            while (lists[i] is None):
                i += 1
                
                # If the index exceeds the number of lists, then break the loop
                if i >= k:
                    return head.next
               
            # Set the i-th value to the minVal with index i 
            minVal = [lists[i].val, i]

            # Increment through each of the remaining linked lists and add the smallest value that the cursor points to the output
            for j in range(i+1, k):

                # Check if the linked list has been exhausted, if not then compare it's value
                if lists[j] is not None:

                    # Check if the first value of the list is less than the min value, if so, replace the value and index of the min value
                    if lists[j].val < minVal[0]:
                        minVal[0] = lists[j].val
                        minVal[1] = j
            
            # Shift backwards the linked list the value was chosen from
            lists[minVal[1]] = lists[minVal[1]].next

            # Add the node to the list
            point.next = ListNode(minVal[0])
            point = point.next
        
        return head.next
