def longest_consecutive(my_list: list[int]) -> int:
    nums = set(my_list)
    longest = 0

    for n in nums:
        if n - 1 not in nums:
            length = 1
            while n + length in nums:
                length += 1
            longest = max(longest, length)

    return longest


def find_missing(my_list: list[int]) -> int:
    if len(my_list) <= 1:
        return None
    n = len(my_list) + 1
    return n * (n + 1) // 2 - sum(my_list)


def find_duplicate(my_list: list[int]) -> int:
    seen = set()
    for x in my_list:
        if x in seen:
            return x
        seen.add(x)


def group_anagrams(words: list[str]) -> list[list[str]]:
    d = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in d:
            d[key] = []
        d[key].append(word)
    return list(d.values())