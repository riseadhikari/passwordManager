import os
import webbrowser
os.system('python db_connect.py')
try:
	argument = input('python manage.py ')
	if argument.strip() == 'runserver':
		os.system(f'python manage.py {argument} 0.0.0.0:19999')
	else:
		os.system(f'python manage.py {argument}')
except KeyboardInterrupt as k:
	pass

try:
	os.remove('config.json')
	with open('config.json','w') as c:
		pass
	os.remove('log.json')
except:
	pass
