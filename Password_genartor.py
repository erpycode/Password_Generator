import random
import secrets


def Pass_word_picker(user_choice):
    count = 1
    Gen_Password = ""
    pass_list = [
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789"
        "!@#$%^&*()-_=+[];:,.?/|﷼,،<ژءِ"
    ]

    while count <= user_choice:
        for i in pass_list:
            Gen_Password += secrets.choice(i)
            count += 1
    print(Gen_Password)
    return Gen_Password


def PassWord_Saver(genpassword):
    with open("Password.txt", "w", encoding="utf-8") as file:
        file.write(genpassword)


user = int(input("lenght of password: "))

Genarated_Password = Pass_word_picker(user)

choice = input("For Saving Your Password Enter y : ")

if choice == "y" or choice == "Y":
    PassWord_Saver(Genarated_Password)
