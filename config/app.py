from flask import Flask
from .boot import Boot
import os


Flask.env = os.environ['FLASK_ENV'] if ('FLASK_ENV' in os.environ) else 'development'
Flask.root = os.path.abspath('.')
Flask.app = app = Flask(__name__,root_path=Flask.root)



# cookie salt config 
app_key_module = __import__("secrets", globals(), locals(), [], 1)
app_key = getattr(app_key_module, Flask.env)

# environment config
environment_config_module = __import__("environments.development", globals(), locals(), ['development'], 1)

# database config
database_module = __import__("database", globals(), locals(), [], 1)
database_config = getattr(database_module, Flask.env)




class AppConfig:
    pass


Flask.app.secret_key = app_key
AppConfig.DATABASE_CONFIG = database_config
Flask.app.config.from_object(AppConfig)
Flask.app.config.from_object(environment_config_module)


Boot.start()


















    