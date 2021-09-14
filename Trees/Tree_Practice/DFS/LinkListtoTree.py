


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class TreeNode():
    def __init__(self, val=None, left_ptr=None, right_ptr=None):
        self.val = val
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr
"""
    Complete the function below.
"""


def sorted_list_to_bst(head):
    """
        Args:
         head(SinglyLinkedListNode_int32)
        Returns:
         TreeNode_in32
    """
