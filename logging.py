#!/usr/bin/env python3

# [...] = process

import os # declare os module
import time # for sleep time
from datetime import date

# Python script to write logs on updates and progress
os.system('clear')
print("\033[1;32;49mtoolaid - Developer Logging Script\n\033[0;37;49m")

def title(): # welcome note
	print('\033[1;31;49m')
	os.system('cat title.txt') #figlet ANSI art for 'toolaid'
	print('\033[0m')

def option():
	print('\033[1;31;49m======================================================  \033[0m')
	print('toolaid commands\n')
	print('[-c]lear   : Clear Terminal')
	print('[-c]ommand : Display toolaid commands')
	print('[-o]ption  : Display options')
	print() 
	print('\033[1;31;49m====================================================== \033[0m')
	print('Select Options\n')
	print('[1] Basic Pentesting/Hacking Tools')
	print('[2] Linux Basic Package Install')
	print('[3] Linux Basic Shell Commands')
	print('\n[5] Developer Mode (mode for devs, which is Dan alone)')
	print('\n\n[0]/[q] Stop toolaid Script')
	print('\nUse the console below')
	print('\n')

def logs(name, date, change, comment): # write entry to log file
	log.write("\nLog Entry [Date] : %s " %(date) )
	log.write("\nUsername         : %s " %(name))
	log.write("\n\n[LOG STATEMENT]\n" )
	log.write(change)
	log.write("\n\n[COMMENT] \n")
	log.write(comment)
	log.write("\n==================================\n\n")

#declare main() function

def main():


	date = os.popen('date').read() #get dat from shell command
	print("==================================")
	print('\n[...] Current date : %s' %(date) )
	print('Press Ctrl+C to return to main script')
	log = open("toolaid.log", "a")
	print('')

	name = input('User name : ')
	change = input('\nChanges made : ')
	comment = input('\nComments : ')

	logs(name, date, change, comment)
	#close connection to file
	log.close() 
	print("")
	time.sleep(0.8)
	print("==================================")
	print("[...] Logging completed \n ")
	input("Press Enter to return")
	os.system('clear')
	title()
	option()
	quit()
	exit()
	



try:
	file = str(os.path.isfile('/home/daniel/Desktop/toolaid/toolaid.log')) #find file availability output true/false


	if file == "False":
		print("Log file Status : \033[1;31;49mUnvailable\033[0;37;49m")
		print("[...] Creating new log file\n")
		log = open("toolaid.log", "x")
		time.sleep(2)
		log = open("toolaid.log", "w")
		log.write("toolaid logs: Activities done on the script\n")
		log.write("================================\n")
		log.close()
		print("[...] Log file has been created")
		input("Press Enter to continue...")
		os.system('clear')
		title()
		print('\033[1;33;40mcoder: dandeviant \033[0;37;40mof \033[1;32;40mUiTM Jasin\033[0;37;40m')
		print('\n  \033[1;31;49mWith great power comes great responsibility')
		print("      \033[1;32;40m- Uncle Ben, who just can't stop getting killed in")
		print("        live-actioname, date, change, commentn Spider-Man movies\033[0;37;40m" )
		option()
		quit()


	else:
		print("Log file status: \033[1;31;49mAvailable\033[0;37;49m")
		#open log file
		log = open("toolaid.log", "a")
		main()
		quit()

except KeyboardInterrupt: # if user use Ctrl+C, which is forbidden...
		print("\033[1;31;49m Bringing you back to main part \033[0;37;49m\n")
		time.sleep(2)
		print("==================================")
		os.system('clear')
		title()
		print('\033[1;33;40mcoder: dandeviant \033[0;37;40mof \033[1;32;40mUiTM Jasin\033[0;37;40m')
		print('\n  \033[1;31;49mWith great power comes great responsibility')
		print("      \033[1;32;40m- Uncle Ben, who just can't stop getting killed in")
		print("        live-action Spider-Man movies\033[0;37;40m" )
		option()
		quit()
		
		



