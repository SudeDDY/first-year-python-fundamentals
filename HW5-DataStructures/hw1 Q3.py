class LinkedSet:
    class _Node:
        __slots__ = ["_element","_next"]                  # Streamline memory usage
        def __init__(self, _element, _next):              # Initialize node's field
            self._element = _element                      # Reference to user's element
            self._next = _next                            # Reference to next node
    def __init__(self):
        self._head = None                                 # Reference to head node
        self._tail = None                                 # Reference to tail node
        self._size = 0
    def __len__(self): 
        return self._size                                 # Checks for lenght
    def is_empty(self):
        return self._size == 0                            # Checks if empty
    def contains(self, e):
        curr = self._head
        while curr is not None:
            if curr._element == e:                        # Checks if it contains or not
                return True
            curr = curr._next
        return False
    def a_readset(self, curr):                            # (a)
        for i in curr:                                    # Read a set of integers and store them in a linked list.
            self.b_insert(i)
    def b_insert(self, e):                                # (b)
        if self.contains(e):                              # Insert an element in an existing set.

            print(f"{e} cannot be inserted as per set rules")
        else:
            new = self._Node(e, None)                     # Create and link new node
            if self.is_empty():
                self._head = new                          # If it is first element
                self._tail = new                          # It is head and tail at the same time
            else:
                self._tail._next = new
                self._tail = new
            self._size += 1
    def c_is_disjoint(self, other):                       # (c)
        curr = self._head                                # Verify whether two sets are disjoint
        while curr is not None:
            if other.contains(curr._element):
                return f"Set-1 & Set-2 are not disjoint, because of common element {curr._element}"
            curr = curr._next
        return f"Set-1 & Set-2 are disjoint"
    def d_intersection(self, other):                      # (d)
        intersects = LinkedSet()                          # Perform intersection of two sets.
        curr = self._head
        while curr is not None:
            if other.contains(curr._element):
                intersects.b_insert(curr._element)
            curr = curr._next
        return intersects
    def d_union(self, other):                             # (d)
        union = LinkedSet()                               # Perform union of two sets.
        curr1 = self._head
        curr2 = other._head
        while curr1 is not None:
            union.b_insert(curr1._element)
            curr1 = curr1._next
        while curr2 is not None:
            if not union.contains(curr2._element):
                union.b_insert(curr2._element)
            curr2 = curr2._next
        return union
    def e_difference(self, other):                        # (e)
        difference = LinkedSet()                          # Perform the set difference between two given sets.
        curr = self._head
        while curr is not None:
            if not other.contains(curr._element):
                difference.b_insert(curr._element)
            curr = curr._next
        return difference
    def __str__(self):                                    # It's about visualization of LinkedLists
        if self.is_empty(): 
            return "{}"
        arr = ""
        start = self._head
        for i in range(self._size):
            arr += str(start._element)
            if i < self._size - 1:
                arr += ", "
            start = start._next
        return "{" + arr + "}"
    def display_as_linked_list(self):
        if self.is_empty():
            return ""
        arr = ""
        start = self._head
        for i in range(self._size):
            arr += str(start._element)
            if i < self._size - 1:
                arr += " -> "
            start = start._next
        return arr
    

if __name__ == "__main__":
    set1 = LinkedSet()                                     # Creating the sets
    set1.a_readset([12, 34, 45, 2, 54])
    print(f"Set-1: {set1}")
    print(f"L1-Set-1: {set1.display_as_linked_list()}")
    
    set2 = LinkedSet()
    set2.a_readset([2, 45, 78, 32])
    print(f"Set-2: {set2}")
    print(f"L2-Set-2: {set2.display_as_linked_list()}")
    
    print("Insert into Set-1: 34")
    set1.b_insert(34)                                      # Trying to insert existing one and getting Error
    print("Insert into Set-1: 99")
    set1.b_insert(99)                                      # Inserting new element
    
    print(f"Set-1: {set1}")
    print(f"L1-Set-1: {set1.display_as_linked_list()}")
    print(f"L2-Set-2: {set2.display_as_linked_list()}")

    print(set1.c_is_disjoint(set2))                        # Checks if disjoint
                                                           # Union, intersection and difference
    print(f"Union of Set-1 and Set-2: {set1.d_union(set2)}")
    print(f"Intersection of Set-1 and Set-2: {set1.d_intersection(set2)}")
    print(f"Set difference Set-1 - Set-2: {set1.e_difference(set2)}")
    print(f"Set difference Set-2 - Set-1: {set2.e_difference(set1)}")
        