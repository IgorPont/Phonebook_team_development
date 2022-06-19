from crud import create, delete, retrive, update, delete
import data_generation


print('Вас приветствует телефонная книга')


def ls_menu() -> int:
    print('МЕНЮ')
    print('1. Показать все записи.')
    print('2. Найти номер по фамилии.')
    print('3. Найти номер по имени.')
    print('4. Поиск по номеру телефона.')
    print('5. Добавить новую запись.')
    print('6. Изменить существующую запись.')
    print('7. Удалить запись.')
    print('8. Закрыть программу.')
    n = int(input('Выберите пункт из меню: '))
    return n


def user_choice(n):
    if n == 1:
        print(retrive())
        # ls_menu()
        # user_choice(ls_menu())
    elif n == 2:
        search = input('Введите фамилию: ')
        retrive(surname= search)
        # ls_menu()
        # user_choice(ls_menu())
    elif n == 3:
        search = input('Введите имя: ')
        retrive(name= search)
        # ls_menu()
        # user_choice(ls_menu())
    elif n == 4:
        search = input('Введите номер  телефона: ')
        retrive(number= search)
        # ls_menu()
        # user_choice(ls_menu())
    elif n == 5:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        number = input('Введите номер телефона: ')
        e_mail = input('Введите электронную почту: ')
        create(name, surname, number, e_mail)  # добавить метод добавления новой записи из CRUD
        # ls_menu()
        # user_choice(ls_menu())
    elif n == 6:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        change = input('Введите номер пункта: ')
        if change == 1:
            search = input('Введите фамилию.')
            retrive(surname= search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            update(id= user_id, new_number= new_number)
            # ls_menu()
            # user_choice(ls_menu())
        elif change == 2:
            search = input('Введите имя: ')
            retrive(name= search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            update(id= user_id, new_number= new_number)
            # ls_menu()
            # user_choice(ls_menu())
        elif change == 3:
            search = input('Введите номер телефона: ')
            retrive(number= search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            update(id= user_id, new_number= new_number)
            # ls_menu()
            # user_choice(ls_menu())
    elif n == 7:
        print('1. Найти номер по фамилии.')
        print('2. Найти номер по имени.')
        print('3. Поиск по номеру телефона.')
        deleting = input('Введите номер пункта: ')
        if deleting == 1:
            search = input('Введите фамилию: ')
            retrive(surname= search)
            user_id = input('Введите id записи: ')
            delete(id= user_id)
            # ls_menu()
            # user_choice(ls_menu())
        elif deleting == 2:
            search = input('Введите имя: ')
            retrive(name= search)
            user_id = input('Введите id записи: ')
            delete(id= user_id)
            # ls_menu()
            # user_choice(ls_menu())
        elif deleting == 3:
            search = input('Введите номер телефона: ')
            retrive(number= search)
            user_id = input('Введите id записи: ')
            new_number = input('Введите новый номер телефона: ')
            delete(id= user_id)
            # ls_menu()
            # user_choice(ls_menu())
    else:
        print('Спасибо за работу!')



# ls_menu()
# def find(user_choice(n)):
# делаем срез по таблице и выдаем необходимые данные Инне.
