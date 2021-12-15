#!/usr/bin/env python3


import signal, os   #declare os and signal module

#declaring option() function
def option():
	print('\033[1;31;49m================================= \033[0m')
	print('\nSelect Tools\n')
	print('[1] Metasploit Framework')
	print('\n\n[0]/[q] Stop toolaid Script')
	print('\nUse the console below')
	print('\n')


#declare helps() function
def helps():
	print('\033[1;31;49m================================= \033[0m')
	print('\n\nManual for toolaid commands\n')
	print('-clear : Clear Terminal')
	print('-help  : Display toolaid command manual')
	print('-option: Display options of tools')
	print()



#declare byebye() funtion
def byebye():
	print("\n\033[1;31;49m\tWhere to contact me: ")
	print('\n\033[1;33;40m\tGitHub : www.github.com/dandeviant')
	print('\033[1;33;40m\tTwitter: www.twitter.com/dandeviant // @dandeviant')
	print('\n\033[1;35;40m\tBye then')
	exit()

#clear terminal with shell command
os.system('clear')


# welcome note
print('====================')
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
			elif (command == '-option') or (command == '-o'): #redisplay options and call option() function
				# os.system('clear')
				option()
			elif (command == '-help') or (command == '-h'):
				helps();
			elif command == '': # if nothing is entered in console
				resume = 3
			else:
				print('Invalid Commands\n') # commands other than ones included in if..else
				resume = 3
	except KeyboardInterrupt: # if user use Ctrl+C, which is forbidden...
		print(" You can't escape... \n")
		main()

main()
