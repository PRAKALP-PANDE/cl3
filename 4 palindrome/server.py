import Pyro4

@Pyro4.expose
class PalindromeSever:
    def is_palindrome(self, s):
        s = s.lower().replace(" ", "") # Convert to lowercase and remove spaces
        return s == s[::-1] # Check if the string is equal to its reverse
    
daemon = Pyro4.Daemon()
uri = daemon.register(PalindromeSever)

print("Sever: ", uri)

daemon.requestLoop()