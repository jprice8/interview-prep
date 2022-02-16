def subarraySum(array, target):
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(array)):
        cur_sum += array[i]
        complement = cur_sum - target 
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1


if __name__ == '__main__':
    array = [1, 3, -3, 8, 5, 7]
    target = 5
    print(subarraySum(array, target))