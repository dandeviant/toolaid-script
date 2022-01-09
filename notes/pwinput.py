# DO NOT name your file with the same name as the imported module
# in this case, the imported module is pwinput
# so, do not rename your file to pwinput.py
# a module calling error will occur and it's truly a pain in the ass to fix

import pwinput


pwd = pwinput.pwinput(mask='?')
print('Your password : %s' %(pwd))
print('\nPassword saved')
