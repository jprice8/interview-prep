def interweavingStrings(one, two, three):

    # while idx3 < len(three):
    #     # String One logic
    #     if idx1 < len(one):
    #         if one[idx1] == three[idx3]:
    #             idx1 += 1
    #             idx3 += 1
    #             continue

    #     # String Two logic
    #     if idx2 < len(two):
    #         if two[idx2] == three[idx3]:
    #             idx2 += 1
    #             idx3 += 1
    #             continue

    #     return False 

    # return True

    if len(three) != len(one) + len(two):
        return False 

    return areInterwoven(one, two, three, 0, 0)


def areInterwoven(one, two, three, i, j):
    k = i + j 
    if k == len(three):
        return True 

    if i < len(one) and one[i] == three[k]:
        if areInterwoven(one, two, three, i + 1, j):
            return True 

    if j < len(two) and two[j] == three[k]:
        return areInterwoven(one, two, three, i, j + 1)

    return False


if __name__ == '__main__':
    one = 'algoexpert'
    two = 'your-dream-job'
    three = 'your-algodream-expertjob'
    print(interweavingStrings(one, two, three))