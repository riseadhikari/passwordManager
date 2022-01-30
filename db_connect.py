from psycopg2 import connect 
from getpass import getpass 



inside = True

while inside:
	try:
		password = getpass()
		# print(password)
		conn = connect(f"dbname=personal user=postgres password={password}")
		with open('.env','w') as env:
			with open('config', 'r') as env_new:
				env.write(env_new.read())
			env.write(f'\nDB_PASSWORD={password}')
		conn.close()
		inside = False
	except Exception as e:
		print(e)
		print('Wrong Password! Try again.')
