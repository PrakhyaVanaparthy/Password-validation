from getpass import getpass
from string import punctuation

def password_validate(password):

    if len(password) < 8:
        print('length should be at least 8')

    if len(password) > 16:
        print('length should be not be greater than 16')

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')

    if check(password):
        print('Password should not be common password')
    else:
	pass

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')

    specialchar = [True for x in password if x in punctuation]
    if len(specialchar) == 0:
	print("Password must contain special character")

def check(password):
    with open('example.txt') as path:
        datafile = path.readlines()
    for line in datafile:
        if password in line:
            return True
    return False

def main():
    password = getpass("Enter Password")
    if (password_validate(password)):
        print("Password is valid")
    else:
        print("Password is invalid!!")

if __name__ == '__main__':
    main()
