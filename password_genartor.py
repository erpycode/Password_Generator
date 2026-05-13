import secrets
import pyperclip
import string


def pass_word_picker(user_choice):
    """this func generate password

    Args:
        user_choice (int): user choose its lenth of pass

    Returns:
        string: generated password
    """
    count = 1
    gen_password = ""
    pass_list = [string.ascii_letters + string.digits + string.punctuation]

    while count <= user_choice:
        for i in pass_list:
            gen_password += secrets.choice(i)
            count += 1
    print(f"\n \n {gen_password}")
    return gen_password


def pass_word_saver(genpassword):
    """this func save gen password to txt file

    Args:
        genpassword (string): password that Generated
    """
    pass_name = input("Enter a name for this password: ")
    with open("Password.txt", "a", encoding="utf-8") as file:
        file.write(f"{pass_name}: {genpassword} \n")


user = int(input("lenght of password (From 8 to 20): "))
if user < 8 or user > 20:
    while user < 8 or user > 20:
        user = int(input("Please Enter Number Between 8 To 20 :  "))
Generated_Password = pass_word_picker(user)
pyperclip.copy(Generated_Password)

choice = input(
    "\n \n ✅ your password copy to clipboard \n \n ُSave your Password? (y/n): "
)

if choice == "y" or choice == "Y":
    pass_word_saver(Generated_Password)
else:
    print("\n ❌ Password not saved.")
