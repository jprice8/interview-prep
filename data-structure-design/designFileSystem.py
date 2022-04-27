import collections


class FileSystem:
    def __init__(self):
        self.paths = collections.defaultdict()

    def createPath(self, path: str, value: int) -> bool:
        # step 1: basic path validation
        if path == '/' or len(path) == 0 or path in self.paths:
            return False 

        # step 2: check for parent
        parent = path[:path.rfind('/')]
        if len(parent) > 1 and parent not in self.paths:
            return False

        # step 3: add path
        self.paths[path] = value 
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path, -1)


def get_hash_index(arr_len: int, path: str) -> int:
    """
    Sum the ASCII codes for each char in path.
    Return the sum mod the arr_len.
    TODO: handle collisions
    """
    ascii_sum = 0
    for char in path:
        ascii_sum += ord(char)

    return ascii_sum % arr_len


if __name__ == '__main__':
    fs = FileSystem()
    print(fs.createPath('/leet', 1))
    print(fs.createPath('/leet/code', 2))
    print(fs.get('/leet/code'))
    print(fs.createPath('/c/d', 1))
    # print(get_hash_index(11, 'Mia'))
