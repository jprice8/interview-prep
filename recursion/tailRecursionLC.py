def sum_non_tail_recursion(myList):
    if len(myList) == 0:
        return 0

    # Not tail recursion because it does some computation after the recursive call returned.
    return myList[0] + sum_non_tail_recursion(myList[1:])


def sum_tail_recursion(ls):
    def helper(ls, acc):
        if len(ls) == 0:
            return acc 
        # Tail recursion because the final instruction is a recursive call.
        return helper(ls[1:], ls[0] + acc)

    return helper(ls, 0)


if __name__ == '__main__':
    # myList = [1, 2, 3]
    # print(sum_non_tail_recursion(myList))

    ls = [1, 2, 3]
    print(sum_tail_recursion(ls))