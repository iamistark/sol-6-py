from collections import defaultdict

def findOriginalArray(changed):
    count = defaultdict(int)

    for num in changed:
        count[num] += 1

    original = []
    for num, freq in count.items():
        if freq % 2 != 0 or freq // 2 > count[num]:
            return []

        original.extend([num // 2] * freq)

    return original
