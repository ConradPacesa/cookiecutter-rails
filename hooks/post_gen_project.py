import os

database = """
default: &default
  adapter: postgresql
  encoding: unicode
  host: db
  username: postgres
  password:
  pool: 5

development:
  <<: *default
  database: myapp_development


test:
  <<: *default
  database: myapp_test"""

if '{{cookiecutter.use_docker}}'.lower() == 'y':
  os.system('docker-compose run web rails new . --force --database=postgresql')
  os.system('docker-compose build')
  with open('./config/database.yml', 'w') as f:
    f.write(database)
  f.close()
  os.system('docker-compose run web rake db:create')
  os.system('docker-compose up')
else: 
  os.system('rails new .')