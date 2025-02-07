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