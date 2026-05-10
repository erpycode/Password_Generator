import random


def Pass_word_picker(user_choice):
    count = 1
    Gen_Password = ""
    pass_list = [
        "@",
        "!",
        "#",
        "$",
        "%",
        "^",
        "&",
        "*",
        "()",
        "+",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "w",
        "y",
        "z",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]

    while count <= user_choice:
        Gen_Password += random.choice(pass_list)
        count += 1
    print(Gen_Password)
    return Gen_Password


user = int(input("lenght of password: "))

Pass_word_picker(user)
