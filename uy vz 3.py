# foydalanuvchi_malumotlari.py

fayl_nomi = "malumotlar.txt"

while True:
    malumot = input("Istalgan ma'lumotni kiriting (to'xtash uchun 'stop' deb yozing): ")

    if malumot.lower() == "stop":
        print("Dastur to'xtatildi.")
        break

    with open(fayl_nomi, "a", encoding="utf-8") as f:
        f.write(malumot + "\n")

    print("Ma'lumot faylga qo'shildi!")