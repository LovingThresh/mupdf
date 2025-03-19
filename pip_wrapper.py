import sys
import os
import subprocess

original_path = list(sys.path)

if '' in sys.path:
    sys.path.remove('')
if '.' in sys.path:
    sys.path.remove('.')

env = dict(os.environ)
if os.name == 'nt': 
    env['PYTHONPATH'] = ';'.join(sys.path)
else:
    env['PYTHONPATH'] = ':'.join(sys.path)

cmd = [sys.executable, '-m', 'pip', 'install', '-vv', '.']
print(f"run command: {' '.join(cmd)}, using PYTHONPATH without .")
sys.stdout.flush()
result = subprocess.run(cmd, env=env, check=False)

sys.exit(result.returncode)
