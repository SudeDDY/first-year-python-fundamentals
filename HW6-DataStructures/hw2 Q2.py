# ─────────────────────────────────────────────
#  CENG112  –  Homework 2   |   Question 2
#  Topic : Binary Search Trees
# ─────────────────────────────────────────────
#  Hardcoded sequences  (do NOT change these)

S1 = [19, 12, 4, 11, 17, 6, 14, 18, 8]
S2 = [8, 18, 14, 6, 17, 11, 4, 12, 19]


# ── TreeNode ──────────────────────────────────
class TreeNode:
    """A node in a binary search tree."""

    def __init__(self, data):
        self.data  = data
        self.left  = None
        self.right = None


# ── BinarySearchTree ──────────────────────────
class BinarySearchTree:
    """Binary Search Tree with traversal, comparison, inversion, and path utilities."""

    def __init__(self):
        self._root = None

    # ── insertion ──────────────────────────

    def insert(self, value):
        """Insert *value* into the BST following BST ordering rules."""
        if self._root is None:
            self._root = TreeNode(value)
        else:
            self._insert_recursive(self._root,value)

    def _insert_recursive(self, node, value):
        """Helper: recursively find the correct position and insert."""
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)

        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

        else: #value == node.data
            pass

    # ── search ──────────────────────────────

    def search(self, value):
        """Return the TreeNode whose data == *value*, or None if not found."""
        return self._search_recursive(self._root, value) #base case

    def _search_recursive(self, node, value):
        """Helper: recursively search for *value*."""
        if node is None:
            return None
        if node.data == value:
            return node
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else: # value>node.data search right
            return self._search_recursive(node.right, value)

    # ── traversals ──────────────────────────

    def inorder(self): #left root right
        """Return a list == result of values produced by an in-order (LNR) traversal."""
        result = []
        self._inorder_recursive(self._root, result)
        return result


    def _inorder_recursive(self, node, result):
        """Helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


    def __str__(self):
        """Display the tree as its in-order traversal."""
        return " -> ".join(str(v) for v in self.inorder())

    # ── equivalence check ───────────────────

    def is_equivalent(self, other):
        """Return True if *self* and *other* are structurally identical and
        contain the same values at every position."""
        return self._equivalent_recursive(self._root, other._root)


    def _equivalent_recursive(self, node1, node2):
        """Helper: recursively compare two subtrees."""
        if node1 is None and node2 is None:
            return  True
        elif node1 is None or node2 is None:
            return False
        elif node1.data != node2.data:
            return False
        else:
            pass
        return (self._equivalent_recursive(node1.left, node2.left) and
            self._equivalent_recursive(node1.right,node2.right))


    # ── inversion ───────────────────────────

    def invert(self):
        """Mirror the tree: swap left and right children at every node."""
        self._invert_recursive(self._root)
        pass

    def _invert_recursive(self, node):
        """Helper: recursively invert subtrees."""
        if node is None:
            pass
        else:
            self._invert_recursive(node.left)
            self._invert_recursive(node.right)

            dummy_variable = node.left
            node.left = node.right
            node.right = dummy_variable


    # ── longest path between two nodes ──────

    def longest_path(self, value1, value2):
        """Return the list of node values on the path from the node with
        *value1* to the node with *value2*.

        The path goes up through the Lowest Common Ancestor (LCA), then down.
        Returns an empty list if either node is not found.
        """
        first_path = self._find_path(self._root, value1)
        second_path = self._find_path(self._root, value2)

        longest = []

        if first_path == None or second_path == None:
            return longest

        i = 0
        while i<len(first_path) and i<len(second_path) and first_path[i]==second_path[i]:
            i+=1

        path_to_lca = first_path[i-1:][::-1] #lca included
        path_from_lca = second_path[i:] #lca not included
        return path_to_lca + path_from_lca


    def _find_path(self, node, value):
        """Return the list of node values from *node* down to the node
        containing *value*, or None if *value* is not in this subtree."""
        list1 = []
        if node is None:
            return  None
        if node.data == value:
            list1.append(node.data)
            return list1

        left_part = self._find_path(node.left, value)
        if left_part is not None:
            list1.append((node.data))
            return list1 + left_part

        right_part = self._find_path(node.right, value)
        if right_part is not None:
            list1.append((node.data))
            return list1 + right_part

        return None



    # ── Euler tour ───────────────────────────

    def euler_tour(self):
        """Return the Euler Tour sequence of the tree as a list of values.

        In an Euler Tour every node is visited:
          • once when first reached (pre-order),
          • once between its left and right subtrees (in-order), and
          • once after both subtrees are done (post-order).
        A leaf node therefore appears three times.
        """
        result = []
        if self._root is None:
            return result
        else:
            self._euler_recursive(self._root, result)
        return result


    def _euler_recursive(self, node, result ): #result as a list
        """Helper: recursively build the Euler tour."""
        result.append(node.data)

        if node.left is not None:
            self._euler_recursive(node.left, result)

        result.append(node.data) #while coming back from left child

        if node.right is not None:
            self._euler_recursive(node.right, result)

        result.append(node.data) #while coming back from right child

# ── Helpers ───────────────────────────────────

def build_bst_from_list(values):
    """Build a BST by inserting *values* one by one in order."""
    binary_tree = BinarySearchTree()
    for i in values:
        binary_tree.insert(i)
    return binary_tree


# ── Main ──────────────────────────────────────

if __name__ == "__main__":

    # (1) Build two BSTs
    t1 = build_bst_from_list(S1)
    t2 = build_bst_from_list(S2)

    print("=== Initial trees (in-order) ===")
    print(f"T1 in-order : {t1}")
    print(f"T2 in-order : {t2}")

    # (2) Check equivalence before inversion
    eq = t1.is_equivalent(t2)
    print(f"\nAre T1 and T2 equivalent? {'Yes' if eq else 'No'}")

    # (3) Invert T1
    t1.invert()
    print(f"\n=== T1 after inversion (in-order) ===")
    print(f"T1 in-order : {t1}")

    # (4) Check equivalence after inversion
    eq_after = t1.is_equivalent(t2)
    print(f"\nAre T1 and T2 equivalent after inverting T1? {'Yes' if eq_after else 'No'}")

    # (5) Longest path between two specific nodes in T1
    node_a, node_b = 4, 18       # feel free to change these values
    path = t1.longest_path(node_a, node_b)
    print(f"\n=== Longest path in T1 from {node_a} to {node_b} ===")
    print(f"Path : {' -> '.join(str(v) for v in path)}")
    print(f"Length : {len(path) - 1} edges")

    # (6) Euler tour of T1
    tour = t1.euler_tour()
    print(f"\n=== Euler Tour of T1 ===")
    print(f"Tour : {' -> '.join(str(v) for v in tour)}")