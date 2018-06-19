import os

app_name = '{{cookiecutter.app_name}}'

shell_script = 'rails new {}'.format(app_name)

os.system(shell_script)