
# VigenereSolver
# Sleethers 2020

import string
import sys
import colorama
from colorama import Fore, Style

# Handle wrong parameter count
if(len(sys.argv) != 3):
	print(Fore.RED + "Wrong amount of parameters")
	print("python3 VigenereSolver.py <cypher-filename> <string_flag>")
	print(Style.RESET_ALL)
	sys.exit(1)

# Handle file containing cypher text
with open(str(sys.argv[1]), 'r') as file:
	cypher = file.read().replace('\n', ' ')

# Assign key and counter variable
key=sys.argv[2]
count = 0;

# Decode vigenere cypher with given key
for i in cypher:
	if(i == ' '):
		print(' ', end='')
		continue

	move = string.ascii_lowercase.index(key[count%len(key)])

	#Handle A-Z and check for left or right shift
	if(ord(i)>=65 and ord(i)<=90):
		if(abs(move) < (ord(i)-64)):
			print(chr(ord(i)-move), end='')
		else:
			print(chr(ord(i)+26-move), end='')
	#Handle a-z and check for left or right shift
	elif(ord(i)>=97 and ord(i)<=122):
		if(abs(move) < (ord(i)-96)):
			print(chr(ord(i)-move), end='')
		else:
			print(chr(ord(i)+26-move), end='')
	else:
		print(i, end='')
		continue
	count+=1

print()
print()
print(Fore.GREEN + "DONE")
print(Style.RESET_ALL)
