from dtc.handlers import GetHandler, RequestError
from dtc.code_lookup import lookup


class LookupHandler(GetHandler):
    def __init__(self):
        super(LookupHandler, self).__init__()
        
    def dtc(self, code):
        try:
            return lookup(code)
        except:
            return []

