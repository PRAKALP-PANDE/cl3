import Pyro4

@Pyro4.expose
class StringConcatentor:
    def concatenate_strings(self, str1, str2):
        return str1 + str2
    
daemon = Pyro4.Daemon()
uri = daemon.register(StringConcatentor)

print(uri)
daemon.requestLoop()