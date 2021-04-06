name = "Fred"
value = 32.387290933

print(name, value)  #  print(str(name), str(value))
print("Next line")
print(name, end=" ")
print(value)
print(name, value, sep='/')
print(name, value, sep= ' + ')

import sys
print("WOW!", name, value, file=sys.stderr)

user_name = input("Please enter user name: ")
print("user_name is", user_name)

from getpass import getpass
password = getpass("Please enter password: ")
print("password is", password)

