from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import crud as cr
import logger as lg


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f'Привет, {update.effective_user.first_name}\nДавай начнем! Введи команду: /main')


async def mein_menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f'Выбери пункт меню, введя соответствующу команду:\n/1 - Показать все записи.\n/2 - Найти номер по фамилии.\n/3 - Найти номер по имени.\n/4 - Поиск по номеру телефона.\n/5 - Добавить новую запись.\n/6 - Изменить существующую запись.\n/7 - Удалить запись.')
    cr.init_data_base('base_phone.csv')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/start - начать сначала\n/main - вызвать главное меню\n/help - вызвать справку')


async def items_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    n = update.message.text
    if n == '/1':
        lg.logging.info('The user has selected item number 1')
        await update.message.reply_text(f'{cr.retrive()}')
    # elif n == '/2':
    #     lg.logging.info('The user has selected item number 2')
    #     search = input('Введите фамилию: ')
    #     lg.logging.info(f'User entered: {search}')
    #     print(cr.retrive(surname=search))
    # elif n == 3:
    #     lg.logging.info('The user has selected item number 3')
    #     search = input('Введите имя: ')
    #     lg.logging.info(f'User entered: {search}')
    #     print(cr.retrive(name=search))
    # elif n == 4:
    #     lg.logging.info('The user has selected item number 4')
    #     search = input('Введите номер  телефона: ')
    #     lg.logging.info(f'User entered: {search}')
    #     print(cr.retrive(number=search))
    elif n == '/5':
        lg.logging.info('The user has selected item number 5')

        await update.message.reply_text(f'Введите имя')
        name = update.message.text
        lg.logging.info(f'User entered: {name}')

        await update.message.reply_text(f'Введите фамилию')
        surname = update.message.text
        lg.logging.info(f'User entered: {surname}')

        await update.message.reply_text(f'Введите номер телефона')
        number = update.message.text
        lg.logging.info(f'User entered: {number}')

        await update.message.reply_text(f'Введите электронную почту')
        email = update.message.text
        lg.logging.info(f'User entered: {email}')
        cr.create(name, surname, number, email)
    # elif n == 6:
    #     lg.logging.info('The user has selected item number 6')
    #     print('1. Найти номер по фамилии.')
    #     print('2. Найти номер по имени.')
    #     print('3. Поиск по номеру телефона.')
    #     change = сhecking_the_number(input('Введите номер пункта: '))
    #     if change == 1:
    #         lg.logging.info('The user has selected item number 6.1')
    #         search = input('Введите фамилию: ')
    #         lg.logging.info(f'User entered: {search}')
    #         cr.retrive(surname=search)
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         new_number = input('Введите новый номер телефона: ')
    #         lg.logging.info(f'User entered: {new_number}')
    #         cr.update(id=user_id, new_number=new_number)
    #     elif change == 2:
    #         lg.logging.info('The user has selected item number 6.2')
    #         search = input('Введите имя: ')
    #         lg.logging.info(f'User entered: {search}')
    #         cr.retrive(name=search)
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         new_number = input('Введите новый номер телефона: ')
    #         lg.logging.info(f'User entered: {new_number}')
    #         cr.update(id=user_id, new_number=new_number)
    #     elif change == 3:
    #         lg.logging.info('The user has selected item number 6.2')
    #         search = input('Введите номер телефона: ')
    #         lg.logging.info(f'User entered: {search}')
    #         cr.retrive(number=search)
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         new_number = input('Введите новый номер телефона: ')
    #         lg.logging.info(f'User entered: {new_number}')
    #         cr.update(id=user_id, new_number=new_number)
    #     else:
    #         lg.logging.info('User entered an invalid menu value')
    #         print(
    #             '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
    # elif n == 7:
    #     lg.logging.info('The user has selected item number 7')
    #     print('1. Найти номер по фамилии.')
    #     print('2. Найти номер по имени.')
    #     print('3. Поиск по номеру телефона.')
    #     deleting = сhecking_the_number(input('Введите номер пункта: '))
    #     if deleting == 1:
    #         lg.logging.info('The user has selected item number 7.1')
    #         search = input('Введите фамилию: ')
    #         lg.logging.info(f'User entered: {search}')
    #         print(cr.retrive(surname=search))
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         cr.delete(id=user_id)
    #     elif deleting == 2:
    #         lg.logging.info('The user has selected item number 7.2')
    #         search = input('Введите имя: ')
    #         lg.logging.info(f'User entered: {search}')
    #         print(cr.retrive(name=search))
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         cr.delete(id=user_id)
    #     elif deleting == 3:
    #         lg.logging.info('The user has selected item number 7.3')
    #         search = input('Введите номер телефона: ')
    #         lg.logging.info(f'User entered: {search}')
    #         print(cr.retrive(number=search))
    #         user_id = input('Введите id записи: ')
    #         lg.logging.info(f'User entered: {user_id}')
    #         new_number = input('Введите новый номер телефона: ')
    #         cr.delete(id=user_id)
    #     else:
    #         lg.logging.info('User entered an invalid menu value')
    #         print(
    #             '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
    # # добавить перезапуск бота или остановку бота
    # # elif n == 8:
    # #     lg.logging.info('End')
    # #     print('Спасибо за работу!')
    # else:
    #     lg.logging.info(f'User entered an invalid menu value: {n}')
    #     print(
    #         '\nТакого пункта меню не существует.\nВведите цифру, соответствующую пункту меню.')
