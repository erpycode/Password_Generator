# Password Generator 🔐

A clean and simple Python tool to generate a strong password, copy it to the clipboard, and optionally save it to a text file.

🌐 [Switch to Persian](README_FA.md)

---

## What this program does

- Prompts the user for a password length between **8 and 20** characters.
- Uses Python's secure `secrets` module to generate random characters.
- Builds a password from lowercase letters, uppercase letters, digits, and symbols.
- Prints the generated password on the screen.
- Copies the password automatically to the clipboard using `pyperclip`.
- If the user agrees, saves the password to a local file named `Password.txt`.

## Requirements

- Python 3.x
- `pyperclip` library

Install the required package with:

```bash
pip install pyperclip
```

## How to run

Run the program from the project folder:

```bash
python Password_genartor.py
```

Then follow the prompts:

1. Enter the desired password length (`8` to `20`).
2. The program generates a secure password.
3. The password is printed and copied to the clipboard.
4. If you type `y`, the password is saved to `Password.txt`.

## Notes

- If you enter a number outside the allowed range, the program will ask again until a valid number is entered.
- The password may include special symbols, so make sure your destination supports them.
- `Password.txt` will be overwritten each time you choose to save.

---

Thank you for using this password generator! 🚀