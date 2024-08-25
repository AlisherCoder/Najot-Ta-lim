import os
import time
import json

def get_info():
    with open('test_fayl.json') as f:
        us = json.load(f)
    return f"Ism: {us['nomi']}\nFamiliya: {us['Fam']}\nRaqam: {us["Raqam"]}\nID: {us['id']}\n"

def renames():
    while True:
        os.system("cls")
        print(get_info())
        print("[1] Ma'lumotlarni tahrirlash.\n"
              "[0] Chiqish.")
        m = input(">>> ")
        match m:
            case '1':
                print("Siz faqat parolni o'zgartirishingiz mumkin.")
                print("Ism-familiya va telefon raqamni o'zgartirish uchun markaz administratsiyasiga murojaat qilishingiz mumkin.")
                while True:
                    a = input("Amaldagi parol. ")
                    if a == '4':
                        y = input("Yangi parol. [Kamida 8 xonali bo'lishi kerak.] ")
                        if len(y)>=8:
                            t = input("Parolni tasdiqlang. ")
                            if y==t:
                                break
                            else:
                                print("Parol tasdiqlanmadi.")
                        else:
                            print("[Kamida 8 xonali bo'lishi kerak.]")
                    else:
                        print("Parol xato.")
                print("Parol yangilandi.")
                time.sleep(2)
            case '0':
                os.system("cls")
                return
            case _:
                print("Xato buyruq berildi.\n")
                time.sleep(2)

def log_in():
    name = "Alisher"
    while True:
        try:
            id = int(input("Id kiriting. "))
            par = int(input("Parol kiriting. "))
            if id == 4 and par == 4:
                os.system("cls")
                print(f"Assalomu alaykum {name}.\n")
                break
            else:
                os.system("cls")
                print("Parol yoki id xato.\n")
        except:
            os.system("cls")
            print("Xato buyruq berildi.\n")

    while True:
        print("[1] Mening kurslarim.\n"
              "[2] Uyga vazifalar.\n"
              "[3] To'lovlarim.\n"
              "[4] Ma'lumotlarim\n"
              "[0] Chiqish.")
        menu = input(">>> ")
        match menu:
            case '1':
                with open('test_fayl.json') as f:
                    user = json.load(f)
                os.system("cls")
                print(user['Kurslar'],'\n')
                button =  input("Chiqish >>> [Enter]")
                os.system("cls")
            case '2':
                os.system("cls")
                print(f"{user['nomi']} Sizga hali uyga vazifa berilmagan.\n")
                button =  input("Chiqish >>> [Enter]")
                os.system("cls")
            case '3':
                os.system("cls")
                print(f"Miqdor: {user["To'lov"]} Turi: {user["Turi"]}\n")
                button =  input("Chiqish >>> [Enter]")
                os.system("cls")
            case '4':
                renames()
                print("Parol yangilandi.")
            case '0':
                os.system("cls")
                return
            case _:
                os.system("cls")
                print("Xato buyruq berildi.\n")
# oxirgi yozilgan kod