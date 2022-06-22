# import data_generation as dg
import user_interface as ui
import logger as lg
import crud


# чисто технически можо получать имя файла бд из переменных среды или конфигурационного файла
# dg.start() # генерация базы контактов
lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()
