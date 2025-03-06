# LOGS: herramienta para capturar eventos

#* Tipos de Eventos:
# DEBUG
# INFO
#* WARNING
#? ERROR
#! CRITICAL

import logging

logging.basicConfig(
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename= '../ClasesPython/Modulo3/02tutoria/registroLog.log',
    filemode= 'w')

logging.debug('Mensaje de depuración')

logging.info('Código iniciado3')