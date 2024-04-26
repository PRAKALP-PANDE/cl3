from xmlrpc.server import SimpleXMLRPCServer

import math

def calc(n1, n2, op):
	if op == 1:
		return n1 + n2;

	elif op == 2:
		return n1 + n2;

	elif op == 3:
		return n1 + n2;

	elif op == 4:
		return n1 + n2;

	else:
		return 1;

with SimpleXMLRPCServer(('localhost, 8000)) as server:
	server.register_function(calc, 'arth')
	print("Running on port 8000")
	server.server_forever()