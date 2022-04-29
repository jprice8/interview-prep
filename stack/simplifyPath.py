class Solution:
    def simplify(self, path: str) -> str:
        stack = [] #
        elements = path.split('/') # ['', 'home', '']
        
        for elem in elements:
            if stack and elem == '..':
                stack.pop()
                continue
            elif elem == '' or elem == '..' or elem == '.':
                continue
                
            stack.append(elem)
            
        result = '/'.join(stack) # home/bar
        return '/' + result

if __name__ == '__main__':
    s = Solution()
    print(s.simplify('/../'))