from hashlib import md5

with open("shadow.txt","r") as shadows:
    with open("Pass_List.txt") as passwords:
        for shadow in shadows:
            for password in passwords:
                hashed=md5(password.strip().encode("UTF-8")).hexdigest()
                if shadow.strip()==hashed:
                    print(f"CRACKED!\n {shadow.strip()} --> {password.strip()}")
               