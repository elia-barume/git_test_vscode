#check number in the pwd
#has lowe case
#has uppe
# rcase
password = input("enter your password")
has_number = False
has_lowercase=False
has_uppercase = False
pwd_length = 0
for char in password:
    pwd_length+=1
    #find the uppercase in the pwd
    if 'A' <= char <='Z':
        has_uppercase = True
        #find the lowercase in the pwd
    elif 'a'<= char <='z':
        has_lowercase = True
        #find a number in the pwd
    elif '0'<= char <= '9':
        has_number = True
#check if the pwd is more than 8 characters
if pwd_length <8:
    print("your password should altealt have 8 characters long")
#check if the pwd has a number, uppercase and lowercase
elif has_number and has_lowercase and has_uppercase:
    print("Strong password")
else:
    print("weak password, your password should atleast contains one uppcase, one lowecase and one digit")

