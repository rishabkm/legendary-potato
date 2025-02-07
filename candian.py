password = input().strip()

lower = upper = digit = 0 

for ch in password:
    if ch.islower():
        lower += 1
    elif ch.isupper():
         upper += 1
    elif ch.isdigit():
         digit += 1

if lower >= 3 and upper >= 2 and digit >= 1:
    print('Valid')

else:
    print('Invalid')             


    password = input()
uppercase = 0
lowercase = 0
digit = 0

if 8 <= len(password) <= 12:
    for i in range(len(password)):
        if password[i].isupper():
            uppercase += 1
        elif password[i].islower():
            lowercase += 1
        elif password[i].isdigit():
            digit += 1

if uppercase >= 2 and lowercase >= 3 and digit >= 1:
    print("Valid")
else:
    print("Invalid")