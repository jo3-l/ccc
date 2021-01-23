from typing import Dict, Optional, List


class SubstitutionRule:
    original: str
    replacement: str

    def __init__(self, original, replacement):
        self.original = original
        self.replacement = replacement

    def apply(s, index):
        return s[0:index]+replacement+s[index + len(original):]


class TrieNode:
    id: Optional[int]  # 1-based ID.
    children: Dict[str, "TrieNode"]
    is_leaf: bool

    def __init__(self, is_leaf, id=None, children={}):
        self.children = children
        self.id = id
        self.is_leaf = is_leaf

    def unwrap_rule(self):
        assert self.is_leaf
        return rules[self.id - 1]


rules: List[SubstitutionRule] = []

# Root node of the trie.
root = TrieNode(False)

# Construct the trie...
for id in range(1, 4):
    original, replacement = input().split(" ")
    rules.append(SubstitutionRule(original, replacement))

    node = root
    for i in range(len(original)):
        char = original[i]
        # Last character, make the new node a leaf and add the ID.
        if i == len(original) - 1:
            if char in node.children:
                node = node.children[char]
                node.is_leaf = True
                node.id = id
                continue

            new_node = TrieNode(True, id)
            node.children[char] = new_node
            node = new_node
            continue

        if char in node.children:
            node = node.children[char]
            continue

        new_node = TrieNode(False)
        node.children[char] = new_node
        node = new_node

num_substitutions = int(input())
source, target = input()

def all_substitutions(s):
    node = root
    matching_nodes = []
    for i in range(len(s)):
        pass