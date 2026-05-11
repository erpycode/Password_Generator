import secrets
import pyperclip


def Pass_Word_Picker(user_choice):
    """this func generate password

    Args:
        user_choice (int): user choose its lenth of pass

    Returns:
        string: generated password
    """
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
    print(f"\n \n {Gen_Password}")
    return Gen_Password


def PassWord_Saver(genpassword):
    """this func save gen password to txt file

    Args:
        genpassword (string): password that Generated
    """
    with open("Password.txt", "w", encoding="utf-8") as file:
        file.write(genpassword)


user = int(input("lenght of password (From 8 to 20): "))
if user < 8 or user > 20:
    while user < 8 or user > 20:
        user = int(input("Please Enter Number Between 8 To 20 :  "))
Generated_Password = Pass_Word_Picker(user)
pyperclip.copy(Generated_Password)

choice = input(
    "\n \n ✅ your password copy to clipboard \n \n ُSave your Password? (y/n): "
)

if choice == "y" or choice == "Y":
    PassWord_Saver(Generated_Password)
else:
    print("\n ❌ Password not saved.")
