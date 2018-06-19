import os

app_name = '{{cookiecutter.app_name}}'

shell_script = 'cd ../ && sh ./generate_app.sh {}'.format(app_name)

os.system(shell_script)