# Simple Password Checker by Aliyu Abdulkadir Baba
password = input("Enter your password: ")

if len(password) < 8:
    print("Weak: Password too short. Use at least 8 characters.")
elif password.isdigit():
    print("Weak: Don't use only numbers.")
else:
    print("Good: Password looks strong. Use MFA too!")
