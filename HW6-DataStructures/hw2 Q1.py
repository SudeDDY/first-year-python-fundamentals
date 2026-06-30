# ─────────────────────────────────────────────
#  CENG112  –  Homework 2   |   Question 1
#  Topic : Linked Lists
# ─────────────────────────────────────────────
#  Hardcoded sequences  (do NOT change these)
S1 = "977593361590535725"
S2 = "81961843034"


# ── Node ─────────────────────────────────────
class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


# ── LinkedList ────────────────────────────────
class LinkedList:
    """Singly linked list with sorting and deduplication support."""

    def __init__(self):
        self._head = None
        self._size = 0

    # ── dunder helpers ──────────────────────

    def __len__(self):
        return self._size

    def __str__(self):
        """Return a human-readable representation: e1 -> e2 -> ... -> eN"""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "[]"

    # ── basic operations ────────────────────

    def append(self, value):
        """Add *value* to the tail of the list."""
        # TODO: implement this method
        newest = Node(value)                             # create new node
        if self._size == 0:                              # if empty, new node is head
            self._head = newest                          
        else:
            current = self._head                         # else, go to the tail and add new node as new tail
            while current.next != None:
                current = current.next
            current.next = newest
        self._size = self._size + 1

    def to_list(self):
        """Return all node values as a plain Python list (head → tail)."""
        # TODO: implement this method
        plainList = []                                    # new empty list
        current = self._head
        while current != None:
            plainList.append(current.data)                # append each node's data into list from linkedlist
            current = current.next
        return plainList


    def from_list(self, lst):
        """Rebuild this linked list from a plain Python list (replaces current content)."""
        # TODO: implement this method
        self._head = None                                 # clean the previous list
        self._size = 0
        for i in lst:
            self.append(i)                                # append each element into linkedlist from list
        return self
    
    # ── sorting ─────────────────────────────

    def quicksort(self):
        """Sort this linked list in ascending order using the Quicksort algorithm.

        The algorithm must operate directly on LinkedList / Node objects.
        Do NOT convert to a Python list or use any built-in sort.
        You must implement the recursive _quicksort helper below and call it here.
        """
        # TODO: implement this method
        self._head = self._quicksort(self._head)          # call recursively


    def _quicksort(self, head):
        """Recursive quicksort on a linked list starting at *head*.

        Pick *head* as the pivot, partition the remaining nodes into two
        sub-lists (less-than and greater-or-equal), recurse on each, then
        concatenate: sorted_left → pivot → sorted_right.

        Returns the new head of the sorted sub-list.
        """
        # TODO: implement this helper
        if head == None or head.next == None:             # partition
            return head
        else:                                            
            pivot = head
            current = head.next
            less_head = None                              
            less_tail = None
            greater_head = None
            greater_tail = None
            while current != None:
                if current.data < pivot.data:
                    if less_head == None:
                        less_head = current
                        less_tail = current
                    else:
                        less_tail.next = current
                        less_tail = current
                if current.data >= pivot.data:
                    if greater_head == None:
                        greater_head = current
                        greater_tail = current
                    else:
                        greater_tail.next = current
                        greater_tail = current
                current = current.next
            if less_tail != None:
                less_tail.next = None
            if greater_tail != None:
                greater_tail.next = None
            pivot.next = None
        sorted_less = self._quicksort(less_head)          # recursion
        sorted_greater = self._quicksort(greater_head) 
        if sorted_less != None:                           # concatenation
            last = self._get_tail(sorted_less)
            last.next = pivot
            pivot.next = sorted_greater
            return sorted_less
        else:
            head = pivot
            pivot.next = sorted_greater
            return pivot

    def _get_tail(self, head):
        """Walk from *head* to the last node and return it.
        Useful for concatenating two sub-lists after partitioning.
        """
        # TODO: implement this helper
        current = head
        while current.next != None:
            current = current.next
        return current

    # ── deduplication ───────────────────────

    def remove_duplicates(self):
        """Remove duplicate values, keeping the first occurrence of each value."""
        # TODO: implement this method
        current = self._head
        while current != None and current.next != None:
            if current.data == current.next.data:         # duplication!
                current.next = current.next.next          # removing duplicate, keeps first occurrence
                self._size -= 1
            else:                                         # this function works for sorted lists
                current = current.next                    # since quicksort() function was called before in "main" part
    # ── merge ───────────────────────────────

    def merge(self, other):
        """Return a *new* LinkedList that contains all elements of *self*
        followed by all elements of *other*."""
        # TODO: implement this method
        new_list = LinkedList()                           # *new* empty LinkedList
        current = self._head 
        while current != None:                            # until current = tail of *self* add into new linkedlist
            new_list.append(current.data)                 # by using pre-defined "append" function
            current = current.next   
        currentt = other._head
        while currentt != None:                           # until currentt = tail of *other* add into new linkedlist
            new_list.append(currentt.data)                # by using pre-defined "append" function
            currentt = currentt.next   
        return new_list                                   # merged 

# ── Helpers ───────────────────────────────────

def build_list_from_string(s):
    """Build a LinkedList whose elements are the individual digits of string *s*
    (each digit stored as an integer)."""
    # TODO: implement this function
    L = LinkedList()                                      # built a linkedlist
    for i in s:
        L.append(int(i))                                  # appended each digit as "integer"
    return L

# ── Main ──────────────────────────────────────

if __name__ == "__main__":

    # (1) Build two linked lists from the digit sequences
    l1 = build_list_from_string(S1)
    l2 = build_list_from_string(S2)

    print("=== Initial lists ===")
    print(f"L1 : {l1}")
    print(f"L2 : {l2}")

    # (2) Sort each list with quicksort
    l1.quicksort()
    l2.quicksort()

    print("\n=== After quicksort ===")
    print(f"L1 : {l1}")
    print(f"L2 : {l2}")

    # (3) Remove duplicates from each list
    l1.remove_duplicates()
    l2.remove_duplicates()

    print("\n=== After removing duplicates ===")
    print(f"L1 : {l1}")
    print(f"L2 : {l2}")

    # (4) Merge the two lists
    merged = l1.merge(l2)

    print("\n=== Merged list (L1 + L2) ===")
    print(f"Merged : {merged}")

    # (5) Sort merged list and remove duplicates once more
    merged.quicksort()
    merged.remove_duplicates()

    print("\n=== Merged list after sort + dedup ===")
    print(f"Merged : {merged}")
