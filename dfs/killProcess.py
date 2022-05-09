from typing import List


class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        def getAllChildren(node, result):
            for childNode in node.children:
                result.append(childNode.val)
                getAllChildren(childNode, result)
        
        
        nodeMap = {}
        
        for process in pid:
            node = Node(process)
            nodeMap[process] = node
            
        for i in range(len(ppid)):
            parentId = ppid[i]
            if parentId == 0:
                continue 
            childId = pid[i]
            
            parentNode = nodeMap[parentId]
            parentNode.children.append(nodeMap[childId])
            
        result = []
        result.append(kill)
        
        getAllChildren(nodeMap[kill], result)
        return result

if __name__ == '__main__':
    pid = [1, 3, 10, 5]
    ppid = [3, 0, 5, 3]
    s = Solution()
    print(s.killProcess(pid, ppid, 5)) # [5, 10]