def get_contacts():
    with open('phonebook.txt', 'r', encoding='utf-8') as file_r:
        content = file_r.read().strip()
        if not content:
            print('*' * 20)
            print('Список контактов пуст или содержит только пустые строки.')
            print('*' * 20)
            return None
        else:
            return content.split('\n\n')


