import crud as cr


print('Вас приветствует телефонная книга\n')


def ls_menu() -> int:
    print('МЕНЮ')
    print('1. Показать все записи.')
    print('2. Найти номер по фамилии.')
    print('3. Найти номер по имени.')
    print('4. Поиск по номеру телефона.')
    print('5. Добавить новую запись.')
    print('6. Изменить существующую запись.')
    print('7. Удалить запись.')
    print('8. Закрыть программу.\n')
    n = int(input('Выберите пункт из меню'))
    return n


def user_choice(n):
    if n == 1:
        print(cr.retrive())
    elif n == 2:
        search = input('Введите фамилию: ')
        cr.retrive(sername=search)
    elif n == 3:
        search = input('Введите имя: ')
        cr.retrive(name=search)
    elif n == 4:
        search = input('Введите номер  телефона: ')
        cr.retrive(number=search)
    elif n == 5:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        number = input('Введите номер телефона: ')
        e_mail = input('Введите электронную почту: ')
        # добавить метод добавления новой записи из CRUD
        cr.create(name, surname, number, e_mail)
    elif n == 6:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        change = input('Введите номер пункта: ')
        if change == 1:
            search = input('Введите фамилию.')
            cr.retrive(sername=search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            cr.update(id=user_id, new_number=new_number)

        elif change == 2:
            search = input('Введите имя: ')
            cr.retrive(name=search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            cr.update(id=user_id, new_number=new_number)
        elif change == 3:
            search = input('Введите номер телефона: ')
            cr.retrive(number=search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            cr.update(id=user_id, new_number=new_number)

    elif n == 7:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        deleting = input('Введите номер пункта: ')
        if deleting == 1:
            search = input('Введите фамилию: ')
            cr.retrive(sername=search)
            user_id = input('Введите id записи: ')
            cr.delete(id=user_id)
        elif deleting == 2:
            search = input('Введите имя: ')
            cr.retrive(name=search)
            user_id = input('Введите id записи: ')
            cr.delete(id=user_id)
        elif deleting == 3:
            search = input('Введите номер телефона: ')
            cr.retrive(number=search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            cr.delete(id=user_id)
    else:
        print('Спасибо за работу!')


ls_menu()
# def find(user_choice(n)):
# делаем срез по таблице и выдаем необходимые данные Инне.
