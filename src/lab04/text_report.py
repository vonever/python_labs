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