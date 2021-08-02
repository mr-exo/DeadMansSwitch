# Dead Man's Switch - Client v1 by exo (https://github.com/mr-exo/)
# Deleting Logs, deleting accounts, sending messages (totally customizable)

# Client Program

try:
	from datetime import datetime
	print("[INFO] Importing Libraries...")
	import time, requests, socket, os
	print("[INFO] Finished!")
except Exception:
	print("[Error] Can't import some of libraries, please try installing them using (pip install -r requirements.txt) or your device/server/computer is not supported.")

def ConnectingToServer(ip,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_address = (ip,port)
	s.connect(server_address)
	details1=input("Enter your login to the server: ")
	details2=input("Enter password: ")
	details=str("0x00"+details1+":"+details2)
	s.send(details.encode())
	while True:
		datb = s.recv(2048)
		bby = datb.decode("utf-8")
		if bby == "HWIDV":
			while True:
				datax = s.recv(2048)
				clean = datax.decode("utf-8")
				if "$" in clean:
					banner=clean.replace("$","")
					print(banner)
					print("Type server.help for list of commands and their usage.")
				command = input(f" [{ip}] > ")
				if clean == "inv_cmd":
					pass
				if command == "disconnect":
					s.send(str.encode("disconnect"))
					s.close()
				else:
					try:
						newdata=command.encode("utf-8")
						s.send(newdata)
					except Exception:
						print("[INFO] Connection closed.")
						break
		elif bby == "nonono":
			print("Bad Credidentials to Server...")
			quit()

#Blocks Of Code
host=str(input("Enter your server's ip address > "))
host_port=int(input("Enter your server's port number > "))
ConnectingToServer(host,host_port)