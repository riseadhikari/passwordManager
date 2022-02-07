from psycopg2 import connect 
from getpass import getpass 
import base64
import json 

inside = True

while inside:
	try:
		password = getpass()
		# print(password)
		conn = connect(f"dbname=personal user=postgres password={password}")
		with open('config.json','w') as env:
			with open('config', 'r') as env_new:
				env.write(env_new.read())
		pass_word = base64.b64encode(password.encode())
		pass_word = pass_word.decode()
		print(pass_word)
		with open('config.json','r') as env1:
			data = json.load(env1)
			# print(data)
			data = dict(data)
			# print(data)
			data["password"] = f"{pass_word}"
		with open('config.json','w') as env2:
			json.dump(data,env2)
			# env.write(f'\nDB_PASSWORD={pass_word}')
		conn.close()
		inside = False
	except Exception as e:
		print(e)
		print('Wrong Password! Try again.')
