from getpass import getpass

def password_validate(password):
    val = True
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

    if len(password) not in range (8, 64):
        print('Password length should be between 8-64 characters')
        val = False

    if check(password):
        print('Password should not be common password')
    else:
	pass

    if not any(char in reg for char in password):
        val = False
	pass
		
    if val:
        return val

def check(password):
    
    #place your common password path below. Or place it in same directory as python code	
    with open('commonpassword.txt') as path:
        datafile = path.readlines()
    for line in datafile:
        if password in line:
            return True
    return False

def main():
    password = getpass("Enter Password")
    print(password)
    if (password_validate(password)):
        print("Password is valid")
    else:
        print("Password is invalid!!")

if __name__ == '__main__':
    main()


