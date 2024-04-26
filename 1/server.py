from xmlrpc.server import SimpleXMLRPCServer

import math

def calc(n):
	return math.factorial(n);

with SimpleXMLRPCServer(('localhost', 8000)) as server:
	server.register_function(calc, 'factorial')
	print("listening at port 8000")
	server.serve_forever()