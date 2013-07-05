import json
import logging
import inspect

from web.webapi import BadRequest
from web import header


class RequestError(Exception):
    pass

def split_parameters(raw_string):
    if not raw_string:
        return {}
    
    parts = raw_string.split('/')
    if len(parts) % 2 == 1:
        parts.append('')
    
    return dict([(parts[i], parts[i + 1]) \
                for i \
                in xrange(len(parts)) \
                if i % 2 == 0])


class HandlerBase(object):
    def GET(self, *args, **kwargs):
        """Return a 400, unless implemented (per spec)."""
    
        return BadRequest()

    def POST(self, *args, **kwargs):
        """Return a 400, unless implemented (per spec)."""

        return BadRequest()

    def json_response(self, data=None):
        header('Content-Type', 'application/json')
        return json.dumps({ 'Error': None, 'Data': data })

    def json_error(self, message, error_type_name, data=None):
        header('Content-Type', 'application/json')
        return json.dumps({ 'Error': error_type_name,
                            'Message': message, 
                            'Data': data })


class GetHandler(HandlerBase):
    def __init__(self, returns_json=True):
        super(GetHandler, self).__init__()
        self.__returns_json = returns_json

    def GET(self, method, ignore_me=None, parameters_raw=None):
        try:
            handler = getattr(self, method)
        except:
            logging.debug("No handler defined for [%s]." % (method))
            return BadRequest()

        parameters = split_parameters(parameters_raw)

        try:
            response = handler(**parameters)
        except Exception as e:
            logging.exception(e)
            
            if issubclass(e.__class__, RequestError):
                message = str(e)
            elif issubclass(e.__class__, TypeError):
                arg_spec = inspect.getargspec(handler)
                arg_names = arg_spec.args[1:]
                defaults = {}
                
                if arg_spec.defaults is not None:
                    default_values = arg_spec.defaults
                    num_default_values = len(default_values)
                    i = 0
                    for k in arg_names[-num_default_values:]:
                        defaults[k] = default_values[i]
                        i += 1
                    
                    arg_names = arg_names[:-num_default_values]
                    
                arg_phrase = ', '.join(arg_names)

                if defaults:
                    if arg_phrase:
                        arg_phrase += ", "
                
                    arg_phrase += ', '.join([(('%s(%s)') % (k, v)) 
                                             for k, v 
                                             in defaults.iteritems()])
                
                message = ("There was an error. Make sure your arguments are "
                          "correct: %s" % (arg_phrase))
            else:
                message = "There was an error."

            return self.json_error(message, e.__class__.__name__) \
                    if self.__returns_json \
                    else message
        else:
            return self.json_response(response)

class Fail(HandlerBase):
    """Receives all requests to bad URLs."""

    pass

