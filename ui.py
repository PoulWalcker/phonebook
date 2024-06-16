from logger import *

def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    with open('backup.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    while command != '5':
        print('''Варианты действий:
        > 1 - Ввод контакта
        > 2 - Вывод контакта  
        > 3 - Поиск контакта
        > 4 - Копирование контакта
        > 5 - Выход
        ''')
        command = input('Введите вариант действия: ')

        while command not in ('1', '2', '3', '4', '5'):
            print('Введены не корректные данные. Введите число от 1 до 5')
            print('''Варианты действий:
            > 1 - Ввод контакта
            > 2 - Вывод контакта  
            > 3 - Поиск контакта 
            > 4 - Копирование контакта
            > 5 - Выход
            ''')
            command = input('Введите вариант действия: ')

        match command:
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contacts()
            case '4':
                copy_contact()
            case '5':
                print('Всего доброго!')
