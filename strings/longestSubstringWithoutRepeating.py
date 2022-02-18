def longestSubstringWithoutRepeating(string):
    stringLength = len(string)
    longestSub = 0
    left = right = 0
    window = set()
    while right < stringLength:
        if string[right] not in window:
            window.add(string[right])
            right += 1
        else:
            window.remove(string[left])
            left += 1
        longestSub = max(longestSub, right - left)
    return longestSub


def takeTwo(string):
    left = 0
    right = 0
    maxLength = 0
    currentMax = 0
    hashMap = {}

    while right < len(string):

        if string[right] not in hashMap:
            hashMap[string[right]] = True
            currentMax += 1
            maxLength = max(maxLength, currentMax)
            right += 1
        else:
            left += 1
            right = left 
            currentMax = 0
            hashMap = {}

    return maxLength


if __name__ == '__main__':
    # string = 'abccabcabcc'
    string = 'abcdbea' # 5
    string1 = 'abcabcbb' # 3
    string2 = 'bbbbb' # 1
    string3 = 'pwwkew' # 3
    print(takeTwo(string))