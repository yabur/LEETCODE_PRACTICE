# Pyhton3 program merge two sorted linked list.
# In third linked list.
# Example
#   input = 1->2->4  , 1->3->4
#   output = 1->1->2->3->4->4
# METHOD: Using Recursive
# Time Complexity:  0(m+n)
# Since we are traversing through the two lists fully. So, the time complexity is O(m+n) where m and n are the lengths of the two lists to be merged.
#

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Constructor to initialize the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Method to print Linked list
    # Traversal operation for linkedlist
    def print_LL(self):
        """
        :return: content of linked list
        """

        temp = self.head
        # There is no node.
        # if temp is None:
        #     print("Linked list is Empty")
        # else:
        #     temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.ref

    # Function to add of node at the end.
    def append(self, new_data):
        # create new node
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        else:
            last = self.head  # need to store the head to the last node allocate a variable for that.

            # takes the head from beginning and travers to last node.
        while last.ref is not None:  # stopping condition.
            last = last.ref
        # now last.ref is None.
        last.ref = new_node


# Function to merge two sorted linked list.
def mergeLists(head1, head2):
    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if head1 is None:
        return head2

    # if List2 is empty then return List1
    if head2 is None:
        return head1

    # If List1's data is smaller or equal to List2's data
    if head1.data <= head2.data:

        # assign temp to List1's data
        temp = head1

        # Again check List1 's data is smaller or equal List
        # Data and call mergeLists function.
        temp.ref = mergeLists(head1.ref, head2)

    else:
        # If List2's data is smaller or equal to List1's data
        # assign temp to List2's data
        temp = head2

        # Again check List2 's data is smaller or equal List
        # Data and call mergeLists function.
        temp.ref = mergeLists(head1, head2.ref)

    # return the temp list.
    return temp


# Driver Function
if __name__ == '__main__':
    # Create linked List:
    # 10->20->30->..
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    # Create linked List:
    # 10->20->30->..
    list2 = LinkedList()
    list2.append(1)
    list2.append(11)
    list2.append(24)
    list2.append(35)
    list2.append(56)

    # Create linked list 3
    list3 = LinkedList()

    # Merge Linked list1 and Linked list2
    # in Linked list3

    list3.head = mergeLists(list1.head, list2.head)

    print(" Merged Linked List is : ", end="")
    list3.print_LL()
