class User:
    def init(self, name, username, email):
        self.name = name
        self.username = username
        self.email = email

class User:
    def init(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.name}, email: {self.email}"



u1 = User("alijon1994", "Alijon Valiyev", "alijon1994@gmail.com")
u2 = User("maria_01", "Maria Karimova", "maria@gmail.com")
u3 = User("botir007", "Botir Usmonov", "botir007@mail.uz")


print(u1.get_info())
print(u2.get_info())
print(u3.get_info())

print(u1.username)
print(u2.email)