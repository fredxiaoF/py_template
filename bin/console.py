#!/usr/bin/env python

import sys
import os
import argparse

sys.path[0] = os.path.abspath(os.path.join(sys.path[0], '..')) 


parser = argparse.ArgumentParser()
parser.add_argument('-H', '--host', type=str, help='host to be bind (default:127.0.0.1)')
parser.add_argument('-p', '--port', type=int, help='port to be listen (default: 5000)')
parser.add_argument('-e', '--environment', type=str, help='the same to specify NODE_ENV (default development)')
args = parser.parse_args()


host = args.host or '127.0.0.1';
port = args.port or 5000 ;
env = args.environment or 'development';


os.environ['FLASK_ENV'] = os.environ['FLASK_ENV'] if 'FLASK_ENV' in os.environ else env


from config.app import Flask




