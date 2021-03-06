#!/usr/bin/env python

import sys
import string
import os

def main():
	number = sys.argv[1]
	scope  = sys.argv[2]

	number = number.replace("-", "")
	number = number.replace(")", "")
	number = number.replace("(", "")

	for char in number:
		if char not in string.digits:
			print ("Error: non-number characters detected in phone number")
			return

	if len(number) < 10:
		print ("Error: phone number is not long enough.")
		return
	elif len(number) == 10:
		number = "+1"+number

	elif len(number) == 11:
		number = "+"+number

	else:
		print ("Error: phone number is too long.")
		return


	scope = scope.lower()

	if scope != "all" and scope != "freezer" and scope != "vivarium":
		print ("Error: scope '"+scope+"' not recognized (accepted values are 'all', 'freezer', and 'vivarium')")
		return

	numberFile = open(os.path.join(os.path.expanduser('~'),"frosti/alertSrc/user_register/phone.txt"), 'a+')

	for line in numberFile:
		if number in line:
			print ("Error: This phone number is already registered in our phone directory!")
			return

	numberFile.write(number+" "+scope+"\n")

	print ("Phone number "+number+" will now receive "+scope+" messages!")

main()
