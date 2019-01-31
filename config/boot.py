import os
import re
import logging
from flask import Flask



class Boot:
    
    @classmethod
    def start(cls):
        cls.__initialize_logger()
        cls.__initialize_script()
        cls.__initialize_routes()
        
    @classmethod
    def __initialize_logger(cls):
        if not Flask.app.config['DEBUG']: return True
        fh = logging.FileHandler("log/%s.log" % (Flask.env))
        formater = logging.Formatter("[%(asctime)s] %(levelname)-5s : %(message)s")
        fh.setFormatter(formater)
        
        if 'DEBUG_LEVEL' in Flask.app.config:
            debug_level = Flask.app.config['DEBUG_LEVEL']
            fh.setLevel(Flask.app.config['DEBUG_LEVEL'])
        
        Flask.app.logger.addHandler(fh)
        
    @classmethod
    def __initialize_script(cls):
        files = os.listdir('config/initializers')
        
        for f in files:
            if re.search(r".py$", f):
                __import__('config.initializers.%s' % (f[0:-3]))
        pass
    
    @classmethod
    def __initialize_routes(cls):
        import config.routes
    
    
    
    
    
    
    
    
    