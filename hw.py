def count_unique_elements(my_list: list) -> int:
    return len(set(my_list))


def remove_duplicates(my_list: list) -> list:
    res = []
    seen = set()
    for x in my_list:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


def reverse_list(my_list: list) -> list:
    return my_list[::-1]


def max_value(my_list: list) -> int:
    return max(my_list)


def min_value(my_list: list) -> int:
    return min(my_list)


def sum_values(my_list: list) -> int:
    return sum(my_list)


def average(my_list: list) -> float:
    return sum(my_list) / len(my_list) if my_list else 0.0


def find_index(my_list: list, element: int) -> int:
    for i, x in enumerate(my_list):
        if x == element:
            return i
    return -1


def is_sorted(my_list: list) -> bool:
    return all(my_list[i] >= my_list[i - 1] for i in range(1, len(my_list)))


def count_frequency(my_list: list, element: int) -> int:
    return my_list.count(element)


def find_mode(my_list: list) -> int:
    if not my_list:
        return None
    freq = {}
    for x in my_list:
        freq[x] = freq.get(x, 0) + 1
    return max(freq, key=freq.get)


def remove_all(my_list: list, element: int) -> list:
    return [x for x in my_list if x != element]


def rotate_left(my_list: list, k: int) -> list:
    if not my_list:
        return []
    k %= len(my_list)
    return my_list[k:] + my_list[:k]


def rotate_right(my_list: list, k: int) -> list:
    if not my_list:
        return []
    k %= len(my_list)
    return my_list[-k:] + my_list[:-k]


def find_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))


def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))


def find_difference(list1: list, list2: list) -> list:
    return list(set(list1) - set(list2))