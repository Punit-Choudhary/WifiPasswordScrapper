#      ******   Wifi Password Scrapper   ******
#   Devloper : Punit

# I took help from GeeksforGeeks and www.docs.python.org to know about more Subprocess module

# wait for my youtube video in which i will explain each and every step ;)
# Here we go!


# Start with importing subprocess module!
import subprocess

data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

# Let's store the profiles by converting them to a list
profiles = [value.split(':')[1][1:-1] for value in data if "All User Profile" in value]

for profile in profiles:
  password = subprocess.check_output(['netsh','wlan','show','profile',profile,'key=clear']).decode('utf-8').split('\n')

# Now sort passwords

  password = [passwd.split(':')[1][1:-1] for passwd in password if "Key Content" in passwd]

# We are all set, now lets print out passwords
  try:
  	print("{:<30}|  {:<}".format(profile,password[0]))
  except IndexError:
  	print("{:<30}|  {:<}".format(profile, ""))