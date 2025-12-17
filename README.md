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

## Лабораторная работа 5

### Задание A

```python
import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """

    json_path = Path(json_path)

    if json_path.exists() == False:
        raise FileNotFoundError
    
    if len(json_path.read_text(encoding = "utf-8")) <= 0:
        raise ValueError

    with json_path.open("r",newline="",encoding = 'utf-8') as f:
        json_import = json.load(f)

    csv_path = Path(csv_path)

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f,fieldnames = ["name",'age','city'])

        csv_writer.writeheader() 
        csv_writer.writerows(json_import)      



def csv_to_json(csv_path: str, json_path: str) -> None:

    json_path = Path(json_path)
    csv_path = Path(csv_path)

    if csv_path.exists() == False:
        raise FileNotFoundError
    
    if len(csv_path.read_text(encoding = "utf-8")) <= 0:
        raise ValueError
    
    list_line_csv = []

    with csv_path.open('r',encoding = 'utf-8') as f:
        csv_read = csv.DictReader(f)
        for line in csv_read:
            list_line_csv.append(line)
    
    with json_path.open("w", newline = '', encoding = "utf-8") as f:
        json_writer = json.dump(list_line_csv,f,ensure_ascii=False, indent = 2)
        
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """

json_to_csv("data/lab05/samples/people.json","data/lab05/out/people_from_json.csv")

csv_to_json("data/lab05/samples/people.csv","data/lab05/out/people_from_csv.json")
```

![json_to_csv_sample](/images/41_json-csv_1.png)

![json_to_csv_out](/images/41_json-csv_2.png)

![csv_to_json_sample](/images/41_json-csv_3.png)

![csv_to_json_out](/images/41_json-csv_4.png)

### Задание B

```python
import openpyxl
from pathlib import Path
import csv

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if csv_path.exists() == False:
        raise FileNotFoundError
    
    if len(csv_path.read_text(encoding = "utf-8")) <= 0:
        return ""
    
    xlsx_book = openpyxl.Workbook()
    xlsx_sheet1 = xlsx_book.active
    xlsx_sheet1.title = "Sheet1"

    with csv_path.open('r',encoding = 'utf-8') as f:
        csv_read = csv.reader(f)
        
        for row in csv_read:
            xlsx_sheet1.append(row)


    xlsx_book.save(xlsx_path)

csv_to_xlsx("data/lab05/samples/people.csv","data/lab05/out/people.xlsx")
```

![csv_sample](/images/41_json-csv_1.png)

![csv_out](/images/42_csv-xlsx.png)

## Лабораторная работа 6

### Задание 1

```python
import sys
sys.path.append("/Users/wheatley0004/Desktop/python_labs")
import argparse
from src.lib.text import count_freq, tokenize, normalize, top_n
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "cat":
        """Реализация команды cat"""

        with Path(args.input).open("r", newline="", encoding="utf8") as f:
            people = f.read()
            list_p = people.split()

        count = 0

        if args.n:
            for peo in list_p:
                count += 1
                print(f"{count} {peo}")

        else:
            for peo in list_p:
                print(f"{peo}")

    elif args.command == "stats":
        """Реализация команды stats"""

        with Path(args.input).open("r", newline="", encoding="utf8") as f:
            people = f.read()

        final = top_n(count_freq(tokenize(normalize(people))), args.top)

        for word, count in final:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()
```

![cat](/images/51_cat.png)

![stats](/images/51_stats.png)

### Задание 2

```python
import sys
sys.path.append("/Users/wheatley0004/Desktop/python_labs")
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv")
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json")
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx")
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    """
        Вызываем код в зависимости от аргументов.
    """

    if args.cmd == "json2csv":
        json_to_csv(Path(args.input), Path(args.output))

    elif args.cmd == "csv2json":
        csv_to_json(Path(args.input), Path(args.output))

    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(Path(args.input), Path(args.output))


if __name__ == "__main__":
    main()
```

![json2csv](/images/52_json2csv.png)

![csv2json](/images/52_csv2json.png)

## Лабораторная работа 7

### Задание А

```python
import csv
import json
from pathlib import Path

import pytest

from src.lib.json_csv import csv_to_json, json_to_csv


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_no_header_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```

### Задание B

```python
import csv
import json
from pathlib import Path

import pytest

from src.lib.json_csv import csv_to_json, json_to_csv


def write_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
    write_json(src, data)

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"}


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8")

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2
    assert set(obj[0]) == {"name", "age"}


def test_json_to_csv_empty_raises(tmp_path: Path):
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_no_header_raises(tmp_path: Path):
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```

### pyproject.toml

```toml
[tool.black]
line-length = 88
target-version = ["py311"]
exclude = """
(
    /venv
  | /.venv
  | /data
  | /images
)
"""

[tool.ruff]
line-length = 88
target-version = "py311"
extend-exclude = ["venv", ".venv", "data", "images"]

[tool.ruff.lint]
select = ["E", "F", "I"]
ignore = ["E501"]
```

### pytest.ini

```ini
[pytest]
addopts = -q
testpaths = tests
```

### Результат

```
black --check .
```

![black](/images/61_black_check.png)

```
ruff check .
```

![ruff](/images/62_ruff_check.png)

### Tests report

![tests_report](/images/63_test_report.png)


## Лабораторная работа 8

### Входной JSON

```json
[
  {
    "fio": "Ivanov Ivan Ivanovich",
    "birthdate": "2000-05-15",
    "group": "SE-01",
    "gpa": 4.2
  },
  {
    "fio": "Petrova Maria Sergeevna",
    "birthdate": "1999-12-03",
    "group": "SE-02",
    "gpa": 3.8
  },
  {
    "fio": "Sidorov Alexey Dmitrievich",
    "birthdate": "2001-08-22",
    "group": "SE-01",
    "gpa": 4.5
  },
  {
    "fio": "Kozlova Ekaterina Vladimirovna",
    "birthdate": "2000-02-29",
    "group": "SE-03",
    "gpa": 4.0
  }
]
```

### Выходной JSON

```json
[
  {
    "fio": "Ivanov Ivan Ivanovich",
    "birthdate": "2000-05-15",
    "group": "SE-01",
    "gpa": 4.2
  },
  {
    "fio": "Petrova Maria Sergeevna",
    "birthdate": "1999-12-03",
    "group": "SE-02",
    "gpa": 3.8
  },
  {
    "fio": "Sidorov Alexey Dmitrievich",
    "birthdate": "2001-08-22",
    "group": "SE-01",
    "gpa": 4.5
  },
  {
    "fio": "Kozlova Ekaterina Vladimirovna",
    "birthdate": "2000-02-29",
    "group": "SE-03",
    "gpa": 4.0
  }
]
```

### Результаты

#### Функция сериализации

![models](/images/71_models.png)

#### Тестовые примеры

![test_examples](/images/72_test_examples.png)


## Лабораторная работа 9

### Результаты

#### Get & add methods

![get_add](/images/81_get_add_methods.png)

#### Search & update & delete methods

![search_update_del](/images/82_search_update_delete_methods.png)

#### Statistics & export to JSON

![stats_export](/images/83_statistics_export2json.png)