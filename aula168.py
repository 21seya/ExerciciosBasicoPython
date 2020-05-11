import sys 

print("print('Ola stdout mundo!')")
print(' Ola stdout mundo!')
input()

print("sys.stdout.write('ola stdout mundo!' + '\\ n')")
sys.stdout.write('Ola stdout mundo! ' + '\\n')
input()

print("input('ola stdin mundo!')")
input('ola stdin mundo!')
input()

print("print('ola stdin mundo!'): sys.stdin.readline()[:-1]")
print('ola stdin mundo!'); sys.stdin.readline()[:-1]
input()
