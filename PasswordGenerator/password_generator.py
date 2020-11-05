import random
import string


digits = list(string.digits*10 + string.ascii_lowercase*10)
uppercase = list(string.ascii_uppercase + string.ascii_lowercase)*30
lowercase = list(string.ascii_lowercase)*30
punct = list(string.ascii_lowercase*10 + string.punctuation*5)

upp_dig = list(string.digits*10 + string.ascii_lowercase*10 + string.ascii_uppercase*10)
upp_dig_pun = list(string.digits*10 + string.ascii_lowercase*10 + string.ascii_uppercase*10 + string.punctuation*5)
digits_pun = list(string.ascii_lowercase*10 + string.digits*10 + string.punctuation*5)
upp_pun = list(string.ascii_lowercase*10 + string.ascii_uppercase*10 +string.punctuation*5)


#Yeah, bad code, but couldn`t come up with a better idea
def generate(LEN,flags=None,how_many=None):
    passwords = []
    U,D,P = None,None,None
    for flag_dict in flags:
        if flag_dict['checkbox'] == 'Upper_reg' and flag_dict['value'] == 'y':
            U = True
        elif flag_dict['checkbox'] == 'Digits' and flag_dict['value'] == 'y':
            D = True
        elif flag_dict['checkbox'] == 'Punctuation' and flag_dict['value'] == 'y':
            P = True

    if U == None and D == None and P == None:
        for password in range(int(how_many)):
            password = random.sample(lowercase ,int(LEN))
            password = ''.join(password)
            passwords.append(password)
        return passwords

    elif U == True and D == None and P == None:
            for password in range(int(how_many)):
                password = random.sample(uppercase ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == None and D == True and P == None:
            for password in range(int(how_many)):
                password = random.sample(digits ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == None and D == None and P == True:
            for password in range(int(how_many)):
                password = random.sample(punct ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == True and D == True and P == None:
            for password in range(int(how_many)):
                password = random.sample(upp_dig ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == None and D == True and P == True:
            for password in range(int(how_many)):
                password = random.sample(digits_pun ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == True and D == None and P == True:
            for password in range(int(how_many)):
                password = random.sample(upp_pun ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords

    elif U == True and D == True and P == True:
            for password in range(int(how_many)):
                password = random.sample(upp_dig_pun ,int(LEN))
                password = ''.join(password)
                passwords.append(password)
            return passwords
    else:
        print("Error!")
