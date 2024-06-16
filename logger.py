from date_create import *
from utils import get_contacts
def add_contact():
    '''
    Вводим контакт и сохраняем в файл
    '''
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding='utf-8') as file_a:
        file_a.write(contact)

def copy_contact():
    contact_index = input('Укажите порядковый номер контакта, который необходимо скопировать: ')

    while contact_index.isalpha():
        print('Ошибка!')
        contact_index = input('Укажите порядковый номер контакта, который необходимо скопировать: ')

    contact_index = int(contact_index) - 1

    list_contacts = get_contacts()

    if 0 <= contact_index < len(list_contacts):
        contact = list_contacts[contact_index]

        print('Выбранный контакт: ')
        print(contact)

        with open('backup.txt', 'a', encoding='utf-8') as file_a:
            file_a.write(f'{contact}\n\n')

        print('Выбранный контакт перенесен в "backup.txt"')
    else:
        print('Такого контакта нет. Попробуйте еще раз!')

# def print_contacts():
#     with open('phonebook.txt', 'r', encoding='utf-8') as file_r:
#         print('\nКонтакты:\n')
#         print(file_r.read())
#         print('\n')
#         print('*' * 30)
#         print('\n')

def print_contacts():

    list_contacts = get_contacts()

    if not list_contacts:
        return

    print('\nКонтакты:')
    print('*' * 20)

    for index, contact in enumerate(list_contacts, 1):
        print(f'{index}. {contact} \n')


    print('*' * 20)

def search_contacts():
    print('''Варианты поиска:
            > 1 - По фамилии
            > 2 - По имени  
            > 3 - По отчеству 
            > 4 - По телефону
            > 5 - По адресу
            ''')
    var = input('Введите вариант поиска: ')

    while var not in ('1', '2', '3', '4', '5'):
        print('Введены не корректные данные. Введите число от 1 до 5')
        var = input('Введите вариант поиска: ')

    index_var = int(var) - 1
    search = input('Введите данные для поиска: ').lower()

    list_contacts = get_contacts()

    if not list_contacts:
        return

    for contact_srt in list_contacts:
        contact_lst = contact_srt.split()
        if search in contact_lst[index_var].lower():
            print(contact_srt)
