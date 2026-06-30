# ─────────────────────────────────────────────
#  CENG112  –  Homework 2   |   Question 3
#  Topic : Recursive Functions
# ─────────────────────────────────────────────

# ── (a) Power Set  ────────────────────────────
# Given set:  S1 = {1, 9, 'A', {2, 'b'}, 78}
# Because Python sets cannot contain mutable types, we represent S1 as a list.
S1 = [1, 9, 'A', (2, 'b'), 78]    # the inner set {2, 'b'} is stored as a tuple


def power_set(s):
    """Return a list of all subsets of *s* (the power set).

    *s* is given as a Python list.  The result must be a list of lists.
    The empty subset [] must be included.

    Example:
        power_set([1, 2]) → [[], [1], [2], [1, 2]]

    Rules:
      • You MUST use recursion – iterative solutions will receive no credit.
      • Do NOT use itertools or any other library for this task.
    """
    if not s:
        return [[]]

    rest_subsets = power_set(s[1:])
    new_subsets = []

    for subset in rest_subsets:
        new_sub = [s[0]] + subset
        new_subsets.append(new_sub)

    return rest_subsets + new_subsets

# ── (b) Permutations ─────────────────────────
STR = "abc"


def permutations(s):
    """Return a list of all permutations of string *s*.

    Example:
        permutations("ab") → ['ab', 'ba']

    Rules:
      • You MUST use recursion – iterative solutions will receive no credit.
      • Do NOT use itertools or any other library for this task.
    """
    if len(s) <=1:
        return [s]

    result = []

    for i in range(len(s)):
        char = s[i]
        remaining_part = s[:i] + s[i+1:]

        for p in permutations(remaining_part):
            result.append(char + p)

    return result



# ── (c) Geometric Sequence ───────────────────
GEO_FIRST_TERM = 1      # a  (first term)
GEO_RATIO      = 2      # r  (common ratio)
GEO_N          = 10     # number of terms to generate


def geometric_sequence(a, r, n):
    """Return a list containing the first *n* terms of the geometric sequence
    with first term *a* and common ratio *r*.

    A geometric sequence satisfies: T(k) = a * r^(k-1)

    Example:
        geometric_sequence(1, 2, 5) → [1, 2, 4, 8, 16]

    Rules:
      • You MUST use recursion – iterative solutions will receive no credit.
    """
    if n <= 0:
        return []
    if n == 1:
        return [a]

    return [a] + geometric_sequence(a*r,r,n-1)


# ── Main ──────────────────────────────────────

if __name__ == "__main__":

    # (a) Power set of S1
    subsets = power_set(S1)
    print("=== (a) Power Set of S1 ===")
    print(f"S1 = {S1}")
    print(f"Number of subsets : {len(subsets)}  (expected {2 ** len(S1)})")
    for subset in subsets:
        print(f"  {subset}")

    print()

    # (b) Permutations of STR
    perms = permutations(STR)
    print("=== (b) Permutations of '{}' ===".format(STR))
    print(f"Number of permutations : {len(perms)}")
    for p in perms:
        print(f"  {p}")

    print()

    # (c) Geometric sequence
    seq = geometric_sequence(GEO_FIRST_TERM, GEO_RATIO, GEO_N)
    print(f"=== (c) Geometric Sequence (a={GEO_FIRST_TERM}, r={GEO_RATIO}, n={GEO_N}) ===")
    print(f"Sequence : {seq}")
