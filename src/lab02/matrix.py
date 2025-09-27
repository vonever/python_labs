def transpose(mat: list):
    index = 0
    for item in mat:
        if len(item) > index:
            index = len(item)
    for item in mat:
        if len(item) != index:
            raise ValueError('рваная матрица')
    res = list()
    if len(mat) == 0:
        return mat
    elif len(mat) == 1:
        for item in mat[0]:
            l = [item]
            res.append(l)
    elif index == 1:
        for item in mat:
            res.append(item[0])
    else:
        for i in range(index):
            l = list()
            for j in range(len(mat)):
                l.append(mat[j][i])
            res.append(l)
    return res

def row_sums(mat: list):
    index = 0
    for item in mat:
        if len(item) > index:
            index = len(item)
    for item in mat:
        if len(item) != index:
            raise ValueError('рваная матрица')
    res = list()
    for item in mat:
        res.append(sum(item))
    return res

def col_sums(mat: list):
    mat = transpose(mat)
    res = list()
    for item in mat:
        res.append(sum(item))
    return res


#transpose
transpose_list1 = [[1, 2, 3]]
transpose_list2 = [[1], [2], [3]]
transpose_list3 = [[1, 2], [3, 4]]
transpose_list4 = []
transpose_list5 = [[1, 2], [3]]
transpose_lists = [transpose_list1, transpose_list2, transpose_list3, transpose_list4, transpose_list5] 
print('transpose:')
for i in range(len(transpose_lists)):
    try:
        print(f'{transpose_lists[i]} -> {transpose(transpose_lists[i])}')
    except ValueError as e:
        print(f'ValueError: {e}')
print()

#row_sums
rowsums_list1 = [[1, 2, 3], [4, 5, 6]]
rowsums_list2 = [[-1, 1], [10, -10]]
rowsums_list3 = [[0, 0], [0, 0]]
rowsums_list4 = [[1, 2], [3]]
rowsums_lists = [rowsums_list1, rowsums_list2, rowsums_list3, rowsums_list4]
print('row_sums:')
for i in range(len(rowsums_lists)):
    try:
        print(f'{rowsums_lists[i]} -> {row_sums(rowsums_lists[i])}')
    except ValueError as e:
        print(f'ValueError: {e}')
print()

#col_sums
colsums_list1 = rowsums_list1
colsums_list2 = rowsums_list2
colsums_list3 = rowsums_list3
colsums_list4 = rowsums_list4
colsums_lists = [colsums_list1, colsums_list2, colsums_list3, colsums_list4]
print('col_sums:')
for i in range(len(colsums_lists)):
    try:
        print(f'{colsums_lists[i]} -> {col_sums(colsums_lists[i])}')
    except ValueError as e:
        print(f'ValueError: {e}')