import os

os.system('python db_connect.py')
try:
	argument = input('python manage.py ')

	os.system(f'python manage.py {argument}')
except KeyboardInterrupt as k:
	pass
try:
	os.remove('.env')
	os.remove('log.json')
	os.rename('.env_new','.env')
except:
	pass