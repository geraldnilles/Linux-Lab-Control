import gpib

DEFAULT_RECV_SIZE = 1000
CHUNK_SIZE = 1000

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


class scope:
	def __init__(self,device_number):
		self.dev = "/dev/usbtmc"+str(device_number)
	
	def send(self,cmd):
		f = open(self.dev,"w")
		f.write(cmd+"\n")
		f.close()

	def recv(self):
		f = open(self.dev,"rb")
		output = f.read()
		f.close()
		return output	


	def send_recv(self,cmd):
		self.send(cmd)
		return self.recv()

	def identify(self):
		return self.send_recv("*IDN?")

	def save_screenshot(self,filename):
		self.send("SAVe:IMAGe:FILEFormat PNG")
		f = open(filename,"wb")
		f.write(self.send_recv("HARDCopy START"))
		f.close()
