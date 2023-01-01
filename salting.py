from getpass import getpass
from bcrypt import hashpw, gensalt, checkpw
passwd = getpass('Password: ').encode()
hashed = hashpw(passwd, gensalt())
print('Hash: ' + hashed)

verify = getpass('Verify password: ').encode()
if (checkpw(verify, hashed)):
    print('It matches!')
else:
    print('Doesn\'t match!')
