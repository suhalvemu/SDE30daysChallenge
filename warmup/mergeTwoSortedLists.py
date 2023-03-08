# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        resultNode = ListNode()

        runningNode = resultNode

        while True:

            if list1 is None:
                runningNode.next = list2
                break

            if list2 is None:
                runningNode.next = list1
                break

            if list1.val < list2.val:
                runningNode.next = list1
                list1 = list1.next

            else:
                runningNode.next = list2
                list2 = list2.next

            runningNode = runningNode.next

        return resultNode.next


if __name__ == '__main__':
    pass
