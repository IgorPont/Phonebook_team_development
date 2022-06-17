import user_interface as ui
import logger as lg
import crud

lg.logging.info('Start')
crud.init_data_base('base_phone.csv') # чисто технически можо получать имя файла бд из переменных среды или конфигурационного файла
ui.ls_menu()
