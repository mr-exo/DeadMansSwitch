# Dead Man's Switch v1 by exo (https://github.com/mr-exo/)
# It can delete Logs, delete accounts, send messages (totally customizable)
# there's an option to ignore you being offline (for X amount of days; it will freeze timer for X amount of days)
# Windows and Linux Supported

# Configuration at 36th line of code

try:
	licznik=0
	ThreadCount = 0

	from datetime import datetime

	x=datetime.now()
	print(f"[{x} - INFO] Starting importing libraries please wait...")

	import time, requests, socket, os, threading
	from _thread import *
	import re

	if os.name == 'nt':
		server_os="Windows"
	else:
		server_os="Linux Kernel"

	x=datetime.now()
	print(f"[{x} - INFO] Finished Loading Libraries!")
	time.sleep(3)

except Exception:

	x=datetime.now()
	print(f"[{x} - Error] Can't import some of libraries, please try installing them using (pip install -r requirements.txt)")

# Dead Man's Switch Configuration
# ==============================
switch_name = "SwitchV1" # Switch name - you can change that to your name or something else
welcome_message_login_page=f"Welcome to {switch_name} ({server_os} v1) !" # Welcome Message on Login page
host_ip="" # Default - socket.gethostname() (<== it will only work in localhost); You can change this to your local ip and port forward your router OR rent a linux server
port_number= 8989 # Default port number is 8989
number_of_users_atst = 3 # max number of users that can be connected at the same time
user="admin" # login to switch
admin_pass="password" # password for user to switch
# ==============================

x=datetime.now()
print(f"[{x} - INFO] ( {server_os} Server Version ) Binding {host_ip}:{port_number} for Server: {switch_name}")

time.sleep(3)

s = socket.socket()

try:
    s.bind((host_ip, port_number))
except socket.error as e:
    print(str(e))
s.listen(number_of_users_atst)

x=datetime.now()
print(f"[{x} - INFO] Listening for connections...")

def multi_threaded_client(connection):
	connection.send(str.encode("RLOG"))
	connection.send(str.encode(f"${welcome_message_login_page}"))
	while True:
		try:
			data = connection.recv(2048)
			clean = data.decode("utf-8")
			if "0x00" in clean:
				hhe=clean.replace("0x00","")
				log,pas=hhe.split(":")
				if log == user:
					if pas == admin_pass:
						connection.send(str.encode("HWIDV"))
					else:
						connection.send(str.encode("nonono"))
						x=datetime.now()
						print(f"[{x} - INFO] Connection Closed with {address[0]} - Disconnect from Client-Side (Invalid Creds)")
						connection.close()
				else:
					connection.send(str.encode("nonono"))
					x=datetime.now()
					print(f"[{x} - INFO] Connection Closed with {address[0]} - Disconnect from Client-Side (Invalid Creds)")
					connection.close()
			if "away" in clean:
				jesus,god=clean.split(".")
				xd=int(god)
				x=datetime.now()
				wynik=int(xd*86400)
				print(f"[{x} - INFO] Sleeping {xd} days = {wynik} seconds | Requested by: {address[0]}")
				time.sleep(wynik)
				connection.send(str.encode("OK"))
			elif "disconnect" in clean:
				x=datetime.now()
				print(f"[{x} - INFO] Connection Closed with {address[0]} - Disconnect from Client-Side.")
				connection.close()
			else:
				if "away" in clean:
					pass
				else:
					connection.send(str.encode("inv_cmd"))
			if not data:
				connection.close()
				break
		except Exception:
			connection.close()
	x=datetime.now()
	print(f"[{x} - INFO] Connection Closed with {address[0]} Due to an Error or Disconnect from Client-Side.")
	connection.close()

while True:
    client, address = s.accept()
    x=datetime.now()
    print(f"[{x} - INFO] Connection from: {address[0]} | Thread {ThreadCount+1}")
    start_new_thread(multi_threaded_client, (client, ))
    ThreadCount += 1
s.close()
