def min_max(n):
    n_sort = list()
    if len(min_max_l) == 0:
        raise ValueError('ValueError')
    else:
        for item in n:
            if '-' in item:
                item1 = item[1:]
            else:
                item1 = item
            if item1.isdigit():
                n_sort.append(int(item))
            else:
                n_sort.append(float(item))
    res = (min(n_sort), max(n_sort))
    return res

def unique_sorted(n):
    n_sort = list()
    for item in n:
        if '-' in item:
            item1 = item[1:]
        else:
            item1 = item
        if item1.isdigit():
            n_sort.append(int(item))
        else:
            n_sort.append(float(item))
    res = sorted(set(n_sort))
    return res

def flatten(n):
    n_flat = list()
    for item in n:
        if not isinstance(item, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        if len(item) > 0:
            for i in range(len(item)):
                n_flat.append(item[i])
    return n_flat
    


#min_max
min_max_l = list(map(str, input('min_max: ').split()))
try:
    min_max_res = min_max(min_max_l)
    print(min_max_res)
except ValueError as e:
    print(e)

#unique_sorted
unique_sorted_l = list(map(str, input('unique_sorted: ').split()))
unique_sorted_res = unique_sorted(unique_sorted_l)
print(unique_sorted_res)

#flatten
flat1 = [[1, 2], [3, 4]]
flat2 = ([1, 2], (3, 4, 5))
flat3 = [[1], [], [2, 3]]
flat4 = [[1, 2], "ab"]
print(f'flatten: {flat3}')
try:
    print(flatten(flat3))
except TypeError as e:
    print(f'TypeError: {e}')