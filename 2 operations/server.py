from xmlrpc.server import SimpleXMLRPCServer

class ArithmeticSever:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y != 0:
            return x/y
        else:
            return "Error: Division by zero"
        
server = SimpleXMLRPCServer(('localhost', 8000))
server.register_instance(ArithmeticSever())

print("Server is running...")
server.serve_forever()