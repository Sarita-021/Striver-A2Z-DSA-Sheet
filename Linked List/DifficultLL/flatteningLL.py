'''Given a linked list containing n head nodes where every node in the linked list contains two pointers:
(i) next points to the next node in the list.
(ii) bottom pointer to a sub-linked list where the current node is the head.
Each of the sub-linked lists nodes and the head nodes are sorted in ascending order based on their data.
Your task is to flatten the linked list such that all the nodes appear in a single level while maintaining the sorted order.

https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1'''


class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        


def merge(list1, list2):
    dummyNode = Node(-1)
    res = dummyNode
    while list1 and list2:
        if list1.data < list2.data:
            res.bottom = list1
            res = list1
            list1 = list1.bottom
        else:
            res.bottom = list2
            res = list2
            list2 = list2.bottom
        res.next = None
    if list1:
        res.bottom = list1
    else:
        res.bottom = list2

    if dummyNode.bottom:
        dummyNode.bottom.next = None

    return dummyNode.bottom
