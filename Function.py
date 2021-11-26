documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people():
    name_result = 'Неверный номер документа'
    document_number = input('Введите номер документа: ')
    for number in documents:
        if document_number in list(number.values())[1]:
            name_result = list(number.values())[2]
    print(name_result)


def shelf():
    shelf_result = 'Неверный номер документа'
    document_number = input('Введите номер документа: ')
    for shelf, number in directories.items():
        if document_number in number:
            shelf_result = f'Номер полки {shelf}'
    print(shelf_result)


def catalog():
    for database in documents:
        print(f'{list(database.values())[0]} "{list(database.values())[1]}" "{list(database.values())[2]}"')


def add():
    new_type = input('Введите тип документа: ')
    new_number = input('Введите номер документа: ')
    new_name = input('Введите имя и фамилию владельца: ')
    shelf_number = input('Введите номер полки: ')
    if directories.get(shelf_number, 0) != 0:
        for shelf, value in directories.items():
            if shelf_number in shelf:
                value.append(new_number)
    else:
        print('Неверный номер полки')
        return
    new_dict = {"type": new_type, "number": new_number, "name": new_name}
    documents.append(new_dict)
    print('Готово!')

def delete():
    document_number = input('Введите номер документа: ')
    number_correct = []
    for shelf, value in directories.items():
        if document_number in value:
            value.remove(document_number)
            number_correct = 'good'
    for record in documents:
        if document_number in record.values():
            documents.remove(record)
    print('Готово!')
    if number_correct != 'good':
        print('Неверный номер документа')


def move():
    document_number = input('Введите номер документа: ')
    new_shelf_number = input('Введите номер целевой полки: ')
    document_correct = []
    if directories.get(new_shelf_number, 0) != 0:
        for shelf, value in directories.items():
            if document_number in value:
                value.remove(document_number)
                document_correct = 'Good'
        directories[new_shelf_number] = document_number
        print('Готово!')
    else:
        print('Неверный номер полки')
    if document_correct != 'Good':
        print('Неверный номер документа')


def add_shelf():
    new_shelf_number = input('Введите номер новой полки: ')
    if new_shelf_number in directories.keys():
        print('Полка уже существует')
        return
    directories[new_shelf_number] = []
    print('Готово!')

user_command = input('Введите команду: ')
if user_command == 'p':
    command = people()
elif user_command == 's':
    command = shelf()
elif user_command == 'l':
    command = catalog()
elif user_command == 'a':
    command = add()
elif user_command == 'd':
    command = delete()
elif user_command == 'm':
    command = move()
elif user_command == 'as':
    command = add_shelf()

