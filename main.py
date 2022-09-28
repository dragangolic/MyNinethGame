from cryptography.fernet import Fernet

'''def write_key():  # fun to store the key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''
# fun. should be def. before it was used


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# key + password + text to encrypt = random text
# random text + key + password = text to encrypt
# if you type wrong password you will have wrong decrypted text

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()  # our strip will strip off the carriage return from our line
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:  # (a mode allows us to add at the end of an existing file,and create \
        # new file if that file does not exists)
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:

    mode = input("Would you like to add new password or view existing one(view, add),"
                 " press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue