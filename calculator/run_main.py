import subprocess

command = ['python', 'main.py', '3 + 7 * 2']
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print('STDOUT:', stdout.decode())
print('STDERR:', stderr.decode())