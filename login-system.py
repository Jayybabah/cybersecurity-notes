# Login System with Lockout - by Aliyu Abdulkadir Baba
# Shows protection against brute-force attacks

correct_password = "Moniepoint123"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")
    if password == correct_password:
        print("Login successful! Welcome, Agent.")
        break
    else:
        attempts += 1
        print(f"Wrong password. You have {3 - attempts} attempts left.")

if attempts == 3:
    print("Account locked! Too many failed attempts. Contact support.")
