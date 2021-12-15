def isPalindrome(stringA):
    rev = ""
    for char in reversed(stringA):
        rev += char 

    if rev == stringA:
        return True 
    else:
        return False

def isPalindrome1(string):
    rev = ""
    for i in reversed(range(len(string))):
        rev += string[i]
    return string == rev

# Avoid string concat for linear instead of quadratic time complexity
def isPalindrome2(string):
    new = []
    for char in reversed(string):
        new.append(char)

    return "".join(new) == string

# Use recursion for O(n) time | O(n) space
def isPalindrome3(string, i=0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome3(string, i + 1)


# Use two pointer close technique
# O(n) time | O(1) space
def isPalindrome4(string):
    i = 0
    j = len(string) - 1

    while i < j:
        left = string[i]
        right = string[j]

        if left != right:
            return False 

        i += 1
        j -= 1

    return True

print(isPalindrome4('abba'))