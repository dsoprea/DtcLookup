from threading import Lock

from dtc.config.ui.stat import COUNTER_FILEPATH
from dtc.handlers import GetHandler, RequestError
from dtc.code_lookup import lookup


class LookupHandler(GetHandler):
    __locker = Lock()

    def __init__(self):
        super(LookupHandler, self).__init__()

    def __increment_counter(self):
            with self.__class__.__locker:
                with file(COUNTER_FILEPATH, 'r') as f:
                    try:
                        value = int(f.read())
                    except ValueError:
                        value = 0

                with file(COUNTER_FILEPATH, 'w+') as f:
                    f.write(str(value + 1))
        
    def dtc(self, code):
        try:
            return lookup(code)
        except:
            return []
        finally:
            self.__increment_counter()

