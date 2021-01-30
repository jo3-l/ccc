from typing import Dict, Optional, List


class SubstitutionRule:
    original: str
    replacement: str
    id: int  # 1-based ID.

    def __init__(self, id, original, replacement):
        self.id = id
        self.original = original
        self.replacement = replacement

    def apply(self, s, index):
        return s[0:index] + replacement + s[index + len(self.original) :]


class TrieNode:
    id: Optional[int]  # Note that this is 1-based.
    children: Dict[str, "TrieNode"]
    is_leaf: bool

    def __init__(self, is_leaf, id=None, children={}):
        self.children = children
        self.id = id
        self.is_leaf = is_leaf

    def unwrap_rule_data(self):
        assert self.is_leaf
        return rules[self.id - 1]


rules: List[SubstitutionRule] = []

root_node = TrieNode(False)

# IDs are 1-based, so we're ranging from [1, 4) instead of [0, 3).
for id in range(1, 4):
    original, replacement = input().split(" ")
    rules.append(SubstitutionRule(id, original, replacement))

    node = root_node
    for i in range(len(original)):
        char = original[i]
        # Last character, make the new node a leaf and add the ID.
        if i == len(original) - 1:
            # We may already have a node at this position - for example, if we
            # handled the substitution rule 'ABC' and then 'AB' right after. In
            # this case, we reuse the node, but simply mark it as a leaf.
            if char in node.children:
                node = node.children[char]
                node.is_leaf = True
                node.id = id
            else:
                # Otherwise, create a new node and set it as a child node.
                new_node = TrieNode(True, id)
                node.children[char] = new_node
                node = new_node
        else:
            # Similar logic if we're not at the end, except these aren't leaf nodes,
            # just normal nodes.

            # If there's already a node here, we do nothing except update the cursor
            # as we're not at the end.
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(False)
                node.children[char] = new_node
                node = new_node
