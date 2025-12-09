import json

data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_json = json.dumps(data)
print("JSON string:", data_json)

talaba_json = '{"ism":"Hasan","familiya":"Husanov","tyil":2000}'
talaba = json.loads(talaba_json)
print("Talaba:", talaba["ism"], talaba["familiya"])

with open("car.json", "w") as f:
    json.dump(data, f)

with open("talaba.json", "w") as f:
    json.dump(talaba, f)

students = [
    {"ism": "Ali", "familiya": "Valiyev", "kurs": 2, "fakultet": "Matematika"},
    {"ism": "Laylo", "familiya": "Karimova", "kurs": 1, "fakultet": "Fizika"},
    {"ism": "Oybek", "familiya": "Ergashev", "kurs": 3, "fakultet": "Informatika"}
]

with open("students.json", "w") as f:
    json.dump(students, f)


with open("students.json") as f:
    loaded_students = json.load(f)

for s in loaded_students:
    print(f"{s['ism']} {s['familiya']}, {s['kurs']}-kurs, {s['fakultet']} talabasi")
    import json


data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
data_json = json.dumps(data)
print("JSON string:", data_json)


talaba_json = '{"ism":"Hasan","familiya":"Husanov","tyil":2000}'
talaba = json.loads(talaba_json)
print("Talaba:", talaba["ism"], talaba["familiya"])


with open("car.json", "w") as f:
    json.dump(data, f)

with open("talaba.json", "w") as f:
    json.dump(talaba, f)


students = [
    {"ism": "Ali", "familiya": "Valiyev", "kurs": 2, "fakultet": "Matematika"},
    {"ism": "Laylo", "familiya": "Karimova", "kurs": 1, "fakultet": "Fizika"},
    {"ism": "Oybek", "familiya": "Ergashev", "kurs": 3, "fakultet": "Informatika"}
]

with open("students.json", "w") as f:
    json.dump(students, f)


with open("students.json") as f:
    loaded_students = json.load(f)

for s in loaded_students:
    print(f"{s['ism']} {s['familiya']}, {s['kurs']}-kurs, {s['fakultet']} talabasi")