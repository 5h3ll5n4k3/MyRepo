from getpass import getpass as gp
from hashlib import md5

def passwd(prompt="Enter your password: "):
    return md5(gp(prompt).encode("UTF-8")).hexdigest()

def login():
    users=[]
    shadows=[]
    while True:
        try:
            with open("shadow.csv", "r") as shadow:

                for line in shadow:
                    users.append(line.split(",")[0])
                    shadows.append(line.split(",")[1].strip())
        except FileNotFoundError:
            print("no shadow file found Please run ShadowFile.py")
            break
        user = input("Enter your username: ")
        if user in users:
            element = users.index(user)
            count=0
            while True:
                count += 1
                password=passwd()
                if password==shadows[element]:
                    print("Logged In.")
                    return True
                elif count ==3:
                    print("Login Failure")
                    break
                else:
                    print("your password did not match")
        else:
            passwd()
            print("your password did not match")
            passwd()
            print("your password did not match")
            passwd()
            print("Login Failure")


if __name__=="__main__":
    login()