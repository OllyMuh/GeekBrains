import json


"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

user_string = input("Введите строку: ")
with open("text.txt", "a") as file:
    while user_string:
        file.write(user_string + "\n")
        user_string = input("Введите строку: ")

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.
"""
with open("text.txt") as file:
    file_strings = file.readlines()
    print(f'Количество строк: ', len(file_strings))
    for string_number, file_string in enumerate(file_strings):
        print(f'Количество слов в строке {string_number} - {len(file_string.split())}')


"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""
total = 0
with open("salary.txt") as file:
    lines = file.readlines()
    number = len(lines)
    print(f"Всего сотрудников {number}")
    for line in lines:
        surname, salary = line.split()
        if int(salary) < 20000:
            print(f"Зарабатывает менее 20000 рублей: {surname}")
        total += int(salary)
print(f"Средний заработок сотрудника: {round(total / number)}")


"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться 
в новый текстовый файл.
"""
dict_translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open("counter.txt") as file_base, open("result.txt", "w") as file_result:
    for line in file_base.readlines():
        text_number, number = line.rstrip().split(" — ")
        file_result.write(f'{dict_translate[text_number]} - {number}\n')

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open("numbers.txt", "w+") as file:
    line = input("Введите числа, разделенные пробелами: ")
    print(line, file=file)
    numbers = line.strip().split()
    numbers_list = [int(number) for number in numbers if number.isdigit()]
    print(sum(numbers_list))


"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
#
dict_shedule = {}
with open("shedule.txt") as file:
    for line in file:
        topic, *lessons = line.split()
        # print(lessons)
        # for lesson in lessons:
        #     if lesson != '—':
        #         number = int(lesson.strip('(л)(пр)(лаб)'))
                # print(number)
        number_lessons = [int(lesson.strip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '—']
        dict_shedule.update({topic.rstrip(':'): sum(number_lessons)})
    print(dict_shedule)


"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма 
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила 
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

dict_average = {}
dict_firms = {}
profit = []
result_list = []
with open("firms.txt") as file:
    for line in file:
        firm, x, vyr, costs = line.rstrip("\n").split()
        profit_firm = int(vyr)-int(costs)
        print(firm, profit_firm)
        if profit_firm > 0:
            dict_firms.update({firm: profit_firm})
            profit.append(profit_firm)
    result_list.append(dict_firms)
    average_profit = sum(profit)/len(profit)
    dict_average.update({"average_profit": average_profit})
    result_list.append(dict_average)
print(result_list)

with open("file.json", "w") as file_json:
    json.dump(result_list, file_json)


