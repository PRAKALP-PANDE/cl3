import xmlrpc.client

# Create a proxy to the XML-RPC server
server_proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get input from the user
try:
    num = int(input("Enter an integer to calculate its factorial: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Call the remote function on the server
result = server_proxy.factorial(num)

# Display the result
print(f"The factorial of {num} is: {result}")
