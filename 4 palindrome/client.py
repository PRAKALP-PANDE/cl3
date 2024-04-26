import Pyro4

uri = input("Enter the uri: ")

palindrome = Pyro4.Proxy(uri)

input_string = input("Enter a string: ")

if palindrome.is_palindrome(input_string):
    print("The string is palindrome")
else:
    print("String is not palindrome.")