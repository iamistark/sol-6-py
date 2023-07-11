def findMaxLength(nums):
    max_length = 0
    count = 0
    count_map = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            count += 1
        else:
            count -= 1

        if count == 0:
            max_length = max(max_length, i + 1)
        elif count in count_map:
            max_length = max(max_length, i - count_map[count])

        if count not in count_map:
            count_map[count] = i

    return max_length
