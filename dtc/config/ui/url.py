import web

from os.path import dirname

import dtc

from dtc import handlers
from dtc.config.ui.general import URL_PREFIX

from dtc.handlers.lookup_handler import LookupHandler

# We used several simpler rules, rather than more ambiguous RXs.
urls = (
    '^/favicon.ico$', 'static_favicon',
    '^/$', 'index',

    '/lookup/([^/]+)(/(.+))?', 'lookup',
    '/(.*)', 'fail',
)

class favicon:
    def GET(self):
        raise web.seeother('/static/images/favicon.ico')

class index:
    def __init__(self):
        self.__content = None

    def __get_content(self):
        if self.__content is None:
            index_filepath = dirname(dtc.__file__) + \
                                '/resource/templates/index.html'
            
            with file(index_filepath) as f:
                content = f.read()
                
                replacements = { 'UrlPrefix': URL_PREFIX }

                web.header('Content-Type', 'text/html')
                self.__content = content % replacements

        return self.__content

    def GET(self):
        return self.__get_content()

mapping = { 'static_favicon': favicon,
            'index': index,
            'fail': handlers.Fail,
            'lookup': LookupHandler,
          }

