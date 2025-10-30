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

### Задание 3

```python
def format_record(rec: tuple):
    name = rec[0].split()
    initials = list()
    for item in range(len(name)):
        name[item] = name[item].capitalize()
        initials.append(name[item][0])
    group = rec[1]
    grade = "{:.2f}".format(rec[2])
    if len(initials) > 2:
        print(f'{str(name[0])} {str(initials[1])}.{str(initials[2])}., гр. {str(group)}, GPA {grade}')
    else:
        print(f'{str(name[0])} {str(initials[1])}., гр. {str(group)}, GPA {grade}')

test1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
test2 = ("Петров Пётр", "IKBO-12", 5.0)
test3 = ("Петров Пётр Петрович", "IKBO-12", 5.0)
test4 = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)

test_list = [test1, test2, test3, test4]
for item in test_list:
    format_record(item)
```

![13_tuples](/images/13_tuples.png)

## Лабораторная работа 3

### Задание 1

```python
import re
from src.lib.text import *

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка", yo2e=True))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

print(top_n(count_freq(["a", "b", "a", "c", "b", "a"]), n=2))
print(top_n(count_freq(["bb", "aa", "bb", "aa", "cc"]), n=2))
```

![A](/images/21_A.png)

### Задание 2

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import *

text = sys.stdin.read()     
textn = text

text = tokenize(normalize(text))
textn = text
top = top_n(count_freq(text), n = 5)
text = top_n(count_freq(text))

print(f"Всего слов: {len(textn)}")
print(f"Уникальных слов: {len(text)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```

![text_stats](/images/22_text_stats.png)

## Лабораторная работа 4

### io_txt_csv

```python
import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encording: str = "utf-8") -> str:
    p = Path(path)
    if p.exists() == False:
        raise FileNotFoundError
    if len(p.read_text(encoding = encording)) <= 0:
        return '' 
    
    return p.read_text(encoding = encording)

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    for i in range (len(rows)-1):
        if len(rows[i]) != len(rows[i+1]):
            raise ValueError
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```

### text_report

```python
from src.lab04.io_txt_csv import *
from src.lib.text import *

#A
a = read_text("/Users/wheatley0004/Desktop/python_labs/data/lab04/input.txt")
a = top_n(count_freq(tokenize(normalize(a))))

write_csv(
    rows = a, 
    path = "/Users/wheatley0004/Desktop/python_labs/data/lab04/report.csv",
    header = ["Word","Count"]  
)

#B
b = read_text("/Users/wheatley0004/Desktop/python_labs/data/lab04/input.txt")
b = tokenize(normalize(b))
b1 = b
b = count_freq(b)
top = top_n(b,5)
b = top_n(b)

write_csv(
    rows = b, 
    path = "/Users/wheatley0004/Desktop/python_labs/data/lab04/report.csv",
    header=["Word","Count"]
)

print(f"Всего слов: {len(b1)}")
print(f"Уникальных слов: {len(b)}")
print("Топ-5:")
for word, count in top:
    print(f"{word}: {count}")
```
### Задание A

![text_report_Aterminal](/images/31_text_report_terminal.png)

![text_report_Ainput](/images/31_text_report_input.png)

![text_report_Acsv](/images/31_text_report_csv.png)

### Задание B

![text_report_Bterminal](/images/32_text_report_terminal.png)

![text_report_Binput](/images/32_text_report_input.png)

![text_report_Bcsv](/images/32_text_report_csv.png)

### Задание C

![text_report_Cterminal](/images/33_text_report_terminal.png)

![text_report_Cinput](/images/33_text_report_input.png)

![text_report_Ccsv](/images/33_text_report_csv.png)