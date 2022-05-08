import collections
from typing import List


class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.content = ''
        self.file = False


class FileSystem:

    def __init__(self):
        self.root = Trie()
        
    def _cleanPath(self, path):
        path = path.strip('/')
        return path.split('/')
    
    
    def _traversePath(self, tokens):
        node = self.root 
        for token in tokens:
            node = node.children[token]
        return node
        
        
    def ls(self, path: str) -> List[str]:
        tokens = self._cleanPath(path)
        # edge case
        if path == '/':
            node = self.root 
        else:
            node = self._traversePath(tokens)
        
        if node.file:
            return [tokens[-1]]
        else:
            res = []
            for name in node.children:
                res.append(name)
            res.sort()
            return res
    
        
    def mkdir(self, path: str) -> None:
        tokens = self._cleanPath(path)
        self._traversePath(tokens)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        tokens = self._cleanPath(filePath)
        node = self._traversePath(tokens)
        
        if node.file:
            node.content += content
        else:
            node.content = content
            node.file = True
            

    def readContentFromFile(self, filePath: str) -> str:
        tokens = self._cleanPath(filePath)
        node = self._traversePath(tokens)
            
        if node.file:
            return node.content


if __name__ == '__main__':
    fs = FileSystem()
    print(fs.ls('/'))
    print(fs.mkdir('/a/b/c'))
    print(fs.addContentToFile('/a/b/c/d', 'hello'))
    print(fs.ls('/'))
    print(fs.readContentFromFile('/a/b/c/d'))