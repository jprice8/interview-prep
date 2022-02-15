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


if __name__ == '__main__':
    # string = 'abccabcabcc'
    string = 'abcdbea'
    print(longestSubstringWithoutRepeating(string))