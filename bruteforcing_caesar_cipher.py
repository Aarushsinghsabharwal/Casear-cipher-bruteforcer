from colorama import Fore
from colorama import init
init()
print(Fore.RED)
print("""
 ___      __      ____   ___      __      ____  
| __|    /  \    | __ | |  _|    /  \    ||  ||
||      / /\ \   ||___  |___    / /\ \   || _||
||__   / /__\ \  | ___|  _  |  / /__\ \  || \\
|___| /_/    \ \ ||___  |___| /_/    \ \ ||  \\  DECODE THE cIpHeR""")
print(Fore.YELLOW)
reference_string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded_message=input("Enter the message to be decrypted:").upper()
original_message=""
for key in range(1,26):
	for letter in encoded_message:
		if letter in reference_string:
			shifted_position=reference_string.find(letter)-(int(key)%26)
			if shifted_position<0:
				shifted_position+=26
			original_char=reference_string[shifted_position]
			original_message+=original_char
		else:
			original_message+=letter
	print(Fore.WHITE+original_message.lower()+'\n')
	original_message=''
