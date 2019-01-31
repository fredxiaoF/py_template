from orator import DatabaseManager
from orator import Model
from flask import Flask
import logging

logger = logging.getLogger('orator.connection.queries')
logger.setLevel(Flask.app.config['DEBUG_LEVEL'])


formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

db = DatabaseManager(Flask.app.config['DATABASE_CONFIG'])
db.set_default_connection('mysql')
Model.set_connection_resolver(db)