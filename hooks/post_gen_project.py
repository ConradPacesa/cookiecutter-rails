import os

app_name = '{{cookiecutter.app_name}}'

if '{{cookiecutter.use_docker}}'.lower() == 'y':
  os.system('docker-compose run web rails new . --force --database=postgresql')
else: 
  os.system('rails new .')