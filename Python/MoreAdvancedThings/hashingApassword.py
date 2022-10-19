from getpass import getpass as gp
from hashlib import md5

# password = gp("enter your password: ")
# print(password)
# encoded=password.encode("UTF-8")
# print(encoded)
# hashed = md5(encoded)
# print(hashed)
# hexed=hashed.hexdigest()
# print(hexed)

# password = md5(gp("Enter your Password: ").encode("UTF-8")).hexdigest()
# print(password)

def passwd(prompt="Enter your password: "):
    return md5(gp(prompt).encode("UTF-8")).hexdigest()

pass1=passwd()
pass2=passwd("Confirm Your password: ")
if pass1==pass2:
    print(f"{pass1}\n{pass2}")
else:
    print("Lobster not happy with password")