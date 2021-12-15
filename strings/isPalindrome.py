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


print(isPalindrome1('abcdcba'))