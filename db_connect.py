from psycopg2 import connect 
from getpass import getpass 
import base64


inside = True

while inside:
	try:
		password = getpass()
		# print(password)
		conn = connect(f"dbname=personal user=postgres password={password}")
		with open('.env','w') as env:
			with open('config', 'r') as env_new:
				env.write(env_new.read())
			pass_word = str(base64.b64encode(password.encode('utf-8')),'utf-8')
			env.write(f'\nDB_PASSWORD={pass_word}')
		conn.close()
		inside = False
	except Exception as e:
		print(e)
		print('Wrong Password! Try again.')
