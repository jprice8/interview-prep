from typing import Any, Dict, List, Optional


class Node:
    def __init__(self) -> None:
        self.children: Dict[str, Node] = {}
        self.value: Optional[Any] = None

def keys_with_prefix(root: Node, prefix: str) -> List[str]:
    results = []
    x = get_node(root, prefix)
    collect(x, list(prefix), results)
    return results


def collect(x: Optional[Node], prefix: List[str], results: List[str]) -> None:
    """
    Append keys under node `x` matching the given prefix to `results`.
    Prefix: list of characters.
    """
    if x is None:
        return
    if x.value is not None:
        prefix_str = ''.join(prefix)
        results.append(prefix_str)
    for c in x.children:
        prefix.append(c)
        collect(x.children[c], prefix, results)
        del prefix[-1]


def get_node(node: Node, key: str) -> Optional[Node]:
    """
    Find Node by key and return node.
    """
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None 

    return node



def searchSuggestions(repository, customerQuery):
    pass


if __name__ == '__main__':
    trie = Trie()