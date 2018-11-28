from urllib.request import urlopen, hashlib
#First, get the hash from the user to get the sha1 hash to crack
sha1hash = input("Please input the hash to crack.\n>")
#Second, we will open a file full of password guesses
LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')
#Third, we will take a guess from the list of passwords we opened, and split it by line
for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
#Fourth, we will hash the guess we took from the password list so we can compare it to the hash the user gave us
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
#Fifth, we will compare the hash the user gave us to the hashed version of the password guess and determine if they are equal
    if hashedGuess == sha1hash:
        print("The password is ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Password guess ",str(guess)," does not match, trying next...")

print("Password not in database, we will get them next time.")
