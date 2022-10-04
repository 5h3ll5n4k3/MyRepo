from getpass import getpass as gp
from hashlib import md5

def passwd(prompt="Enter your password: "):
    return md5(gp(prompt).encode("UTF-8")).hexdigest()

def main():
    user = input ("Enter what you want your user name to be: ")
    while True:
        pass1=passwd()
        pass2=passwd("confirm password:")
        if pass1==pass2:
            with open("shadow.csv","a") as shadow:
                shadow.write(f"{user},{pass1}\n")
            break
        else:
            print("your passwords did not match")

if __name__=="__main__":
    main()
