'''
if you're not Daniel, pls ignore this. The script don't use this one :)

to check if figlet is installed 
'''

import apt, time
cache = apt.Cache()
cache.open()

print ("=======================================")
print('checking figlet')
time.sleep(1)
response = "figlet installed."
try:
    cache['figlet'].is_installed
except KeyError:
    response = "figlet isn't installed."

print(response)
