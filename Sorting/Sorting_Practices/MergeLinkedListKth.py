class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


'''
    The function accepts an ARRAY of SinglyLinkedListNodes as input 
    and is expected to return a SinglyLinkedListNode.

    Complete the function below.
'''

import heapq


def merge_k_lists(lists):
    all_nodes = list()

    for l in lists:
        while l:
            all_nodes.append(l.data)
            l = l.next

    output = None

    for j in sorted(all_nodes):
        if not output:
            output = SinglyLinkedListNode(j)
            curr = output
            continue
        curr.next = SinglyLinkedListNode(j)
        curr = curr.next

    return output





def merge_kth_lists(lists):
    all_node_vals = []

    for list in lists:
        while list:
            all_node_vals.append(list.data)
            list = list.next
    all_node_vals.sort()
    current_head = head = SinglyLinkedListNode(0)

    for val in all_node_vals:
        current_head.next = SinglyLinkedListNode(val)
        current_head = current_head.next

    return head.next

def merge_kt_lists(lists):

    all_nodes = []
    head = ll = SinglyLinkedListNode(0)
    for l in lists:
        while l:
            all_nodes.append(l.data)
            l = l.next
    for x in sorted(all_nodes):
        ll.next = SinglyLinkedListNode(x)
        ll = ll.next
    return head.next