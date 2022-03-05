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
        if self.is_empty():
            return 0
        
        nodes = 0
        current = self.head
        while current is not None:
            current = current.next
            nodes += 1
            
        return nodes

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # If self.is_empty() == True set the head and the tail to the new node
        if self.head is None:
            self.head = node
            self.tail = node
        # Else append node after tail


        # add new node to end (after tail node), update tail so that the new node = tail
        else:
            self.tail.next = node
            self.tail = node
            

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.is_empty():
            # list is empty, node becomes both head and tail
            self.head = node
            self.tail = node
        else:
            # head becomes node.nxt which means that the head is now the node
            node.next = self.head #whaterver is next to the node is now self.head so everything scoots over
            self.head = node #node is now the first thing in line



    def find(self, item):
        """Return an item from this linked list if it is present.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item, if present return True otherwise False
        node = self.head

        while node is not None:

            # if item == item
            if node.data == item:
                return True
            # moves node next in line to keep looping until item has been found
            node = node.next
         
        return False

    def previous_node(self, node):
        '''Returns the previous node given a node'''
        current = self.head #starts with head

        while current is not None:
            if current.next is node: #if the next node matches, then current node is node.previous
                return current
            current = current.next
        raise ValueError(f'Node {node} not exist')

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item

        # if item doesn't exist or self is empty, return error
        if not self.find(item) or self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
        
        # self is one item, delete everything
        if self.head.data == item and self.tail.data == item:
            self.head = None
            self.tail = None
            return
        
        # item is head, assign the next item head so that it starts then
        if self.head.data == item:
            self.head = self.head.next
            return
        
        # item is tail so look for previous and asign it the role of tail
        if self.tail.data == item:
            self.tail = self.previous_node(self.tail)
            self.tail.next = None
            return
        
        current = self.head
        while current is not None:
            if current.data == item:
                self.previous_node(current).next = current.next
                return
            current = current.next
        
        raise Exception('Something aint right')
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

if __name__ == "__main__":
    my_ll = LinkedList(["A", "B", "C"])
    print(my_ll)
    

    


