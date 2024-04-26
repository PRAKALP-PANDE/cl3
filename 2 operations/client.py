import xmlrpc.client

def main():
    server_proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))
    operation = input("Choose operation (add/sustract/multiply/divide): ").lower()

    if operation == 'add':
        result = server_proxy.add(x, y)
    elif operation == 'subtract':
        result = server_proxy.subtract(x, y)
    elif operation == 'multiply':
        result = server_proxy.multiply(x, y)
    elif operation == 'divide':
        result = server_proxy.divide(x, y)
    else:
        result = "Invalid Operation"

    print("Result: ", result)

if __name__ == "__main__":
    main()