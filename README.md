## Лабораторная работа 1

### Задание 1

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![01_greeting](/images/01_greeting.png)

### Задание 2

```python
a = input('a: ').replace(',', '.')
b = input('b: ').replace(',', '.')
a = float(a)
b = float(b)
print(f'sum={"{:.2f}".format(a+b)}; avg={"{:.2f}".format((a+b)/2)}')
```

![02_sum_avg](/images/02_sum_avg.png)

### Задание 3

```python
price = float(input('Цена: '))
discount = float(input('Скидка: '))
vat = float(input('НДС: '))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

text = ['База после скидки:', 'НДС:', 'Итого к оплате:']
nums = ["{:.2f}".format(base), "{:.2f}".format(vat_amount), "{:.2f}".format(total)]

for text, nums in zip(text, nums):
    print(f'{text:<{20}} {nums:>{1}} ₽')
```

![03_discount_vat](/images/03_discount_vat.png)

### Задание 4

```python
mins = int(input('Минуты: '))
hrs = mins//60
mins %= 60
print(f'{hrs}:{mins:02d}')
```

![04_minutes_to_hhmm](/images/04_minutes_to_hhmm.png)

### Задание 5

```python
name = input('ФИО: ')
name = name.split()
initials = [name[i][0] for i in range(len(name))]
initials = ''.join(initials)

name = ' '.join(name)
symbols = len(name)

print(f'Инициалы: {initials}.')
print(f'Длина символов: {symbols}')
```

![05_initials_and_len](/images/05_initials_and_len.png)


## Лабораторная работа 2

### Задание 1

```python
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
#выбираем любой из вариантов
print(f'flatten: {flat4}')
try:
    print(flatten(flat4))
except TypeError as e:
    print(f'TypeError: {e}')
```

![11_arrays_test1](/images/11_arrays_test1.png)

![11_arrays_test2](/images/11_arrays_test2.png)

![11_arrays_test3](/images/11_arrays_test3.png)

![11_arrays_test4](/images/11_arrays_test4.png)

### Задание 2

```python
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
```

![12_matrix](/images/12_matrix.png)