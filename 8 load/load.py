class Server:
	def __init__(self, name):
		self.name = name

	def req(self):
		print(f"running {self.name} ")

servers = [Server(f" server {i} ") for i in range (1, 4)]

curr = 0

for _ in range(10):
	server = servers[curr]
	server.req()
	curr = (curr + 1) % len(servers)