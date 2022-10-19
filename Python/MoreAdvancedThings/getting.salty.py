from hashlib import md5, sha512
from getpass import getpass as gp

def old_way(prompt= "Enter your password: "):
    return md5(gp(prompt).encode('UTF-8')).hexdigest()


print(old_way())

def salted(prompt="Enter your password: "):
    return sha512("".join(
        ("SaltThatHash",gp(prompt),"NoPwn4u")
    ).encode('UTF-8')).hexdigest()


print(salted())

def passwd(user, prompt='Enter your password: '):
    salt= md5(user.encode('UTF-8')).hexdigest()
    return sha512("".join(
        ("SaltThatHashNoPwn4u", gp(prompt),salt)
            ).encode("UTF-8")).hexdigest()

user = input("Enter your user name: ")
print(passwd(user))