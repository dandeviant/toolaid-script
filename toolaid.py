#!/usr/bin/env python3


import signal, os   #declare os and signal module
import time			#declare time module

#declaring option() function
def option():
	print('\033[1;31;49m====================================================== \033[0m')
	print('Select Tools\n')
	print('[1] Basic Pentesting/Hacking Tools')
	print('[2] Linux Basic Package Install')
	print('[3] Linux Basic Shell Commands')
	print('\n[5] Developer Mode (mode for )')
	print('\n\n[0]/[q] Stop toolaid Script')
	print('\nUse the console below')
	print('\n')


#declare helps() function
def helps():
	print('\033[1;31;49m======================================================  \033[0m')
	print('toolaid commands\n')
	print('-clear : Clear Terminal')
	print('-help  : Display toolaid command manual')
	print('-option: Display options of tools')
	print()



#declare byebye() funtion
def byebye():
	print("\n\033[1;31;49m\tI don't hide myself :). You can find me here :")
	print('\n\033[1;33;49m\tGitHub : www.github.com/dandeviant')
	print('\033[1;33;49m\tTwitter: www.twitter.com/dandeviant // @dandeviant')
	print('\n\033[1;35;49m\tBye then')
	exit()

#clear terminal with shell command
os.system('clear')


# welcome note
print('\033[1;31;49m')
os.system('figlet -f Bloody toolaid') #figlet ANSI art for 'toolaid'
print('\033[0m')
print('\033[1;33;40mcoder: dandeviant \033[0;37;40mof \033[1;32;40mUiTM Jasin\033[0;37;40m')
print('\n\033[1;31;49mWith great power comes great responsibility')
print("      \033[1;32;40m- Uncle Ben, who just can't stop getting killed in")
print("        live-action Spider-Man movies\033[0;37;40m" )


helps()
option()



def main(): # main body of the script input
	try:
	#list of if else statement for commands entered
		resume = 3
		while resume == 3:	
			command = input('toolaid > ')    # input interface
			if (command == '0') or (command == 'q'):	#exit program
				byebye()	
			elif (command == '-clear') or (command == '-c'): 	#clear screen 	
				os.system('clear')
				print('Enter -option to display the options\n')

			#redisplay options and call option() function
			elif (command == '-option') or (command == '-o'): 
				# os.system('clear')
				option()

			elif (command == '-help') or (command == '-h'):
				helps();

			# if nothing is entered in console
			elif command == '': 
				resume = 3

			#enter developer mode
			elif command == '5': 
				print("Entering developer mode")
				time.sleep(2)
				os.system("python3 toolaid.py")
			#invalid commands
			else:
				print('Invalid Commands\n') # commands other than ones included in if..else
				resume = 3
	except KeyboardInterrupt: # if user use Ctrl+C, which is forbidden...
		print("\033[1;31;49m You can't just escape like that... \033[0;37;49m\n")
		main()

main()
