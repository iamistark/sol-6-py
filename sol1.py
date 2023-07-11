def findPermutation(s):
    n = len(s)
    perm = []
    start, end = 0, n

    for c in s:
        if c == 'I':
            perm.append(start)
            start += 1
        elif c == 'D':
            perm.append(end)
            end -= 1

    # Append the final value
    perm.append(start)

    return perm



