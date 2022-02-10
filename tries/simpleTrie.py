class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s, idx):
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx + 1)