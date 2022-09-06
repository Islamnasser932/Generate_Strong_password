# 1-> import string module
# 2->store all char in list (upper / lower / digit / punc)
# 3-> take number of char from user
# 4-> make sure num of char > 6
# 5-> suffle list
# 6-> calc 30% , 20 %
# 7-> create pass


import string
import random


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.ascii_letters)
s4 = list(string.digits)
s5 = list(string.punctuation)

charcter_number = input(" How many charcter do you want for the password ? :")

while True:
    try:
        charcter_number = int(charcter_number)
        if charcter_number < 6:
            print("please enter at least 10 number ")
            charcter_number = input("please enter a nuumber again :")

        else:
            break
    except:
        print(" enter number only ")
        charcter_number = input(
            " How many charcter do you want for the password ? :")


random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
random.shuffle(s5)

part1 = round(charcter_number * (30/100))
part2 = round(charcter_number * (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
    password.append(s3[i])


for i in range(part2):
    password.append(s4[i])
    password.append(s5[i])


random.shuffle([password])

password = "".join(password[0:])

print(password)
