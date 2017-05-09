# Exercises 3.3

# item = 90
# a_list = [20, 44, 48, 55, 62, 66, 74, 88, 93, 99]


def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    if len(a_list) == 0:
        return '{item} was not found in the list'.format(item=item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return '{item} found'.format(item=item)
        else:
            if a_list[i] < item:
                return binary_search(a_list[i+1:], item)
            else:
                return binary_search(a_list[:i], item)

