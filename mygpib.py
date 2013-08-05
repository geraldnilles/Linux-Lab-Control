import gpib

DEFAULT_RECV_SIZE = 1000

class device:
	def __init__(self,gpib_address,card=0):

		self.device = gpib.dev(card,gpib_address)

		# TODO Check for errors

	def send(self,cmd):
		return gpib.write(self.device,cmd)
	
	def recv(self,size=DEFAULT_RECV_SIZE):
		return gpib.read(self.device,size)


	def send_recv(self,cmd,size=DEFAULT_RECV_SIZE):
		self.send(cmd)
		return self.recv(size)

	# TODO Add destructor that kill connection


class Agilent_6626A(device):
	def set_voltage(self,channel):
		pass

	def set_current(self,channel):
		pass

	def read_voltage(self,channel):
		pass

	def read_current(self,channel):
		pass


