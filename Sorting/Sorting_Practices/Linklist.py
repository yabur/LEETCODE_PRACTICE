# Definition for singly-linked list.
# Example
#   input = 1->2->4  , 1->3->4
#   output = 1->1->2->3->4->4
#

# Initialization of the fields of the node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Initialize Linkedlist. It will contain the link.
class LinkedList:
    def __init__(self):
        self.head = None  # all about link

    # Traversal operation for linkedlist
    def print_LL(self):
        """
        :return: content of linked list
        """
        # There is no node.
        if self.head is None:
            print("Linked list is Empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data)
                temp = temp.ref

    '''
    Three nodes have been created.
     We have references to these three blocks as head,
            second and third

            llist.head	 second			 third
                |			 |				 |
                |			 |				 |
            +----+------+	 +----+------+	 +----+------+
            | 1 | None |	 | 2 | None |	 | 3 | None |
            +----+------+	 +----+------+	 +----+------+
            '''

    # llist.head.next = second;  # Link first node with second

    '''
            Now next of first Node refers to second. So they
            both are linked.

            llist.head	 second			 third
                |			 |				 |
                |			 |				 |
            +----+------+	 +----+------+	 +----+------+
            | 1 | o-------->| 2 | null |	 | 3 | null |
            +----+------+	 +----+------+	 +----+------+
            '''

    # second.next = third;  # Link second node with the third node

    '''
            Now next of second Node refers to third. So all three
            nodes are linked.

            llist.head	 second			 third
                |			 |				 |
                |			 |				 |
            +----+------+	 +----+------+	 +----+------+
            | 1 | o-------->| 2 | o-------->| 3 | null |
            +----+------+	 +----+------+	 +----+------+
    '''

    # Time complexity is 0(1)
    def add_begin(self, new_data):
        """
        ADDS NODE TO THE LINKEDLIST FROM BEGINNING
        :param new_data:
        :param self:
        :return:
        """
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)

        # 3: Make ref of new Node as head
        new_node.ref = self.head
        # 4. Move the head to po point to new Node
        self.head = new_node

    # Time complexity is O(n). Since there is a loop from head to end.
    # Optimized : O(1) by using second pointer to the tail of linked list
    def add_end(self, new_data):

        # 1. Create new node
        # 2. Put in the data
        # 3. Set ref as None
        new_node = Node(new_data)

        # 4. If the Linked list is empty,the make the new node as head
        if self.head is None:
            self.head = new_node
            return
        #  5. Else traverse till the last node (go to last node) whatever the ref store in last node called last.
        last = self.head

        while last.ref is not None:
            # increment to reference
            last = last.ref

        # 6. Change the ref of last node
        last.ref = new_node

    '''
    Three nodes have been created.
     We have references to these three blocks as head,
            
            llist.head	 prev_node	 	     last_node
                |			     |				 |
                | 1010			 | 2100		     | 3300
            +----+------+	 +----+------+	 +----+------+
            | 1 | 2100 |	 | 2 | 3300 |	 | 3 | None |
            +----+------+	 +----+------+	 +----+------+
            
            Insert Between prev_node and last_node
        new_node
            |(..)
            |
            +----+------+
            | 4 | None |    ref will be 3300 for new node.
            +----+------+
            '''

    # This function is in LinkedList class.
    # Inserts a new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */

    def add_after(self, prev_node, new_data):
        # 1. Check if the given data exits
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)

        # 4. Make "ref" of new Node as "ref" of prev_node
        new_node.ref = prev_node.ref

        # 5. Make reference of prev_node as new_node
        prev_node.ref = new_node


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

llist.add_end(6)
llist.print_LL()
