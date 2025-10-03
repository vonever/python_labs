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