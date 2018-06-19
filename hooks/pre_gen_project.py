import subprocess

app_name = '{{cookiecutter.app_name}}'

shell_script = '../generate_app.sh {}'.format(app_name)

subprocess.call(shell_script)