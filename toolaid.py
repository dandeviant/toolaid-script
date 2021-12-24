#!/usr/bin/env python3


import signal, os   #declare os and signal module
import time			#declare time module

#declaring option() function
def option():
	print('\033[1;31;49m======================================================  \033[0m')
	print('toolaid commands\n')
	print('[-c]lear   : Clear Terminal')
	print('[-o]ption  : Display options')
	print() 
	print('\033[1;31;49m====================================================== \033[0m')
	print('Select Options\n')
	
	# hacking tools not used as of now, uncomment later
	# print('[1] Basic Pentesting/Hacking Tools')


	print('[2] Linux Basic Package Install')
	print('[3] Linux Basic Shell Commands')
	print('\n[5] Developer Mode (mode for devs, which is Dan alone)')
	print('\n\n[0]/[q] Stop toolaid Script')
	print('\nUse the console below')
	print('\n')
	



#declare byebye() funtion
def byebye():
	print("\n\033[1;31;49m\tI don't hide myself :). You can find me here :")
	print('\n\033[1;33;49m\tGitHub : www.github.com/dandeviant')
	print('\033[1;33;49m\tTwitter: www.twitter.com/dandeviant // @dandeviant')
	print('\n\033[1;35;49m\tBye then\033[0m')

def title(): # welcome note
	print('\033[1;31;49m')
	os.system('cat title.txt') #figlet ANSI art for 'toolaid'
	print('\033[0m')
	print('\033[1;33;40mcoder: dandeviant \033[0;37;40mof \033[1;32;40mUiTM Jasin\033[0;37;40m')
	print('\n  \033[1;31;49mWith great power comes great responsibility')
	print("      \033[1;32;40m- Uncle Ben, who just can't stop getting killed in")
	print("        live-action Spider-Man movies\033[0;37;40m" )
	

def main(): # main body of the script input
	try:
	#list of if else statement for commands entered
		resume = 3

		while resume == 3:	
			command = input('toolaid > ')    # input interface
			if (command == '0') or (command == 'q'):	#exit program
				byebye()
				quit()

			elif (command == '-clear') or (command == '-c'): 	#clear screen 	
				os.system('clear')
				print('Enter [-o]ption to display the options\n')

			#redisplay options and call option() function
			elif (command == '-option') or (command == '-o'): 
				# os.system('clear')
				option()

			# if nothing is entered in console
			elif command == '': 
				resume = 3

			#enter developer mode
			elif command == '5': 
				print("[...] Entering developer logging mode")
				time.sleep(2)
				os.system("python3 logging.py")

			#invalid commands
			else:
				print('Invalid Commands\n') # commands other than ones included in if..else
				resume = 3

	except KeyboardInterrupt: # if user use Ctrl+C, which is forbidden...
		print("\033[1;31;49m You can't just escape like that... \033[0;37;49m\n")
		main()

#clear terminal with shell command
os.system('clear')



title()
if os.geteuid() != 0:
	print('\n================================================')
	username = os.popen('whoami').read()
	print("Current user: %s" %(username))
	print("\033[1;35;49mThis script gonna run lots of installing.")
	print("So, the script needs superuser access.")
	print('\033[1;31;49m')
	print('Please try again with "sudo". Bye')
	print('\033[0m')
else:
	option()
	main()
