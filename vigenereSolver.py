
# VigenereSolver
# Sleethers 2020

import string
from string import ascii_lowercase
import sys
import colorama
from colorama import Fore, Style
from itertools import chain,product

# Handle wrong parameter count
if(len(sys.argv) > 3):
	print(Fore.RED + "Wrong amount of parameters")
	print("python3 VigenereSolver.py <cypher-filename> <string_flag>")
	print("python3 VigenereSolver.py <cypher-filename> : SEARCHES THE falg BY BRUTE FORCE")
	print(Style.RESET_ALL)
	sys.exit(1)

# Handle file containing cypher text
with open(str(sys.argv[1]), 'r') as file:
	cypher = file.read().replace('\n', ' ')

# Decode vigenere cypher with given key
def solve_vigenere(key, printsol = False):
	count = 0;
	solution = ""
	for i in cypher:
		if(i == ' '):
			solution+=' '
			continue

		move = string.ascii_lowercase.index(key[count%len(key)])

		#Handle A-Z and check for left or right shift
		if(ord(i)>=65 and ord(i)<=90):
			if(abs(move) < (ord(i)-64)):
				solution+=chr(ord(i)-move)
			else:
				solution+=chr(ord(i)+26-move)
		#Handle a-z and check for left or right shift
		elif(ord(i)>=97 and ord(i)<=122):
			if(abs(move) < (ord(i)-96)):
				solution+=chr(ord(i)-move)
			else:
				solution+=chr(ord(i)+26-move)
		else:
			solution+=i
			continue
		count+=1
	if(printsol):
		print(solution)
		print(Fore.GREEN + "SOLVING - DONE")
		print(Style.RESET_ALL)
	return solution

def brute_force():
	for chars in chain(ascii_lowercase, product(ascii_lowercase, repeat=2),product(ascii_lowercase, repeat=3),product(ascii_lowercase, repeat=4),product(ascii_lowercase, repeat=5),product(ascii_lowercase, repeat=6),product(ascii_lowercase, repeat=7)):
		if all(x in solve_vigenere(''.join(chars)) for x in [" the ", " for ", " is ", " are ", " to "]):
			print(''.join(chars))

if(len(sys.argv) == 3):
	print(Fore.MAGENTA + "START_SOLVING" + Style.RESET_ALL)
	key=sys.argv[2]
	solve_vigenere(key,True)
elif(len(sys.argv) == 2):
	print(Fore.MAGENTA + "STARTING_BRUTE_FORCE" + Style.RESET_ALL)
	brute_force()






