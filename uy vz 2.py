class Shaxs:
    odamlar_soni = 0

    def init(self, ism, yosh):
        self.__ism = ism
        self.__yosh = yosh
        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism

    def set_ism(self, yangi_ism):
        self.__ism = yangi_ism

    def get_yosh(self):
        return self.__yosh

    def set_yosh(self, yangi_yosh):
        self.__yosh = yangi_yosh

    def info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"

    @classmethod
    def get_odamlar_soni(cls):
        return cls.odamlar_soni


class Talaba(Shaxs):
    talabalar_soni = 0

    def init(self, ism, yosh, fakultet):
        super().init(ism, yosh)
        self.__fakultet = fakultet
        Talaba.talabalar_soni += 1

    def get_fakultet(self):
        return self.__fakultet

    def set_fakultet(self, yangi_fakultet):
        self.__fakultet = yangi_fakultet

    def info(self):
        return f"{super().info()}, Fakultet: {self.__fakultet}"

    @classmethod
    def get_talabalar_soni(cls):
        return cls.talabalar_soni



s1 = Shaxs("Ali", 40)
t1 = Talaba("Oybek", 20, "Informatika")
t2 = Talaba("Nilufar", 19, "Matematika")

print(s1.info())
print(t1.info())
print("Odamlar soni:", Shaxs.get_odamlar_soni())
print("Talabalar soni:", Talaba.get_talabalar_soni())