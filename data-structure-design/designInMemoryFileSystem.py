import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = collections.defaultdict(TrieNode)
        self.isFile = False 

    def __repr__(self) -> str:
        return repr(self.children)


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        path_lst = path.split("/")
        node = self.root
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        if node.isFile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans

    def mkdir(self, path: str) -> None:
        path_lst = path.split("/")
        node = self.root
        for p in path_lst:
            if not p:
                continue 
            node = node.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        path_lst = filePath.split("/")
        node = self.root 
        for p in path_lst:
            if not p:
                continue 
            node = node.children[p]
        node.content += content 
        node.isFile = True 

    def readContentFromFile(self, filePath: str) -> str:
        path_lst = filePath.split("/")
        node = self.root
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        return node.content


if __name__ == '__main__':
    f = FileSystem()

    print(f.ls("/")) # []

    print(f.mkdir("/a/b/c"))

    print(f.addContentToFile("/a/b/c/d", "hello"))

    print(f.ls("/")) # return ["a"]

    print(f.readContentFromFile("/a/b/c/d")) # return "hello"