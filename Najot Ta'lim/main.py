from login import log_in
import os
import time
os.system('cls')
print("Najot Ta'limga xush kelibsiz.\n")
while True:
    print("[1] Admin panel.\n"
          "[2] Kurslar haqida ma'lumot.\n"
          "[3] Kirish.\n"
          "[0] Chiqish.")
    menu = input(">>> ")
    match menu:
        case '1':
            pass
        case '2':
            pass
        case '3':
            log_in()
        case '0':
            break
        case _:
            print("Xato buyruq berildi.\n")
            time.sleep(1)
            os.system('cls')
# Oxirgi yozilgan kod