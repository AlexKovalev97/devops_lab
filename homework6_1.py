import json
import os
import subprocess
import yaml
python_v = str(subprocess.Popen("python -V",
                                shell=True, stdout=subprocess.PIPE).
               communicate()[0].decode('utf-8').strip())
# name (alias)
v_env = str(os.environ['VIRTUAL_ENV'])
ex = str(os.environ['__PYVENV_LAUNCHER__'])
pip_v = str(subprocess.Popen("pip -V",
                             shell=True, stdout=subprocess.PIPE).
            communicate()[0].decode('utf-8').strip())
path = str(os.environ['PYTHONPATH'])
pip_l = str(subprocess.Popen("pip list",
                             shell=True, stdout=subprocess.PIPE).
            communicate()[0].decode('utf-8').strip())
# site-pack loc
l_json = []
l_yaml = []
dict_out = {
    'Version': python_v,
    'Environment': v_env,
    'Executable': ex,
    'PIP version': pip_v,
    'Python path': path,
    'Packages': pip_l.split('\n'),
}
l_json.append(dict_out)
with open('output.json', 'w') as js:
    json.dump(l_json, js, indent=2)

l_yaml.append(dict_out)
with open('output.yaml', 'w') as yl:
    yaml.dump(l_yaml, yl, default_flow_style=False)
