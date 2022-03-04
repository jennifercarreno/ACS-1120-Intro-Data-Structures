#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable, moves to next opening/slot?
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        while self.head is not None:
            self.head = self.head.next
            length +=1
       
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        new_node = Node(item)
        # If self.is_empty() == True set the head and the tail to the new node
        if self.is_empty() == True:
            self.head = new_node
            self.tail = new_node
        # Else append node after tail
        # add new node to end (after tail node), update tail so that the new node = tail

        else:
            self.tail.next = new_node
            self.tail = new_node
            

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if not self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.head.data = new_node
        else:
            new_node = self.head
            self.tail = new_node
            self.head.data = new_node
            self.tail.data = new_node



    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False

        while not self.is_empty():
            if self.node.data == item:
                return True
            else: 
                return False

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item

        if self.find(item):

            if self.head.data == item and self.tail.data == item:
                    self.head = None
                    self.tail = None
                    return
            
            if self.head.data == item:
                    self.head = self.head.next
                    return
                
            if self.tail.data == item:

                node = self.head
                while node is not None:
                    if node.next is item:
                        self.tail = node
                    else: 
                        node = node.next

                self.tail.next = None
                return
        else: 
                raise ValueError('Item not found: {}'.format(item))

        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)
    

    


