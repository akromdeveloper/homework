class Fan:
    def init(self, nomi, daraja=None):
        self.nomi = nomi
        self.daraja = daraja

    def repr(self):
        return f"Fan({self.nomi})"

    def get_info(self):
        if self.daraja:
            return f"{self.nomi} (daraja: {self.daraja})"
        return self.nomi


class Shaxs:
    def init(self, ism, yosh=None):
        self.ism = ism
        self.yosh = yosh

    def get_info(self):
        info = f"Ism: {self.ism}"
        if self.yosh:
            info += f", Yosh: {self.yosh}"
        return info


class Talaba(Shaxs):
    def init(self, ism, yosh=None, fakultet=None):
        super().init(ism, yosh)
        self.fanlar = []          # bo‘sh ro‘yxat
        self.fakultet = fakultet

    def fanga_yozil(self, fan: Fan):
        if any(f.nomi == fan.nomi for f in self.fanlar):
            return f"Siz allaqachon {fan.nomi} faniga yozilgansiz"
        self.fanlar.append(fan)
        return f"Siz {fan.nomi} faniga muvaffaqiyatli yozildingiz"

    def remove_fan(self, fan_nomi: str):
        for f in self.fanlar:
            if f.nomi == fan_nomi:
                self.fanlar.remove(f)
                return f"{fan_nomi} fani o‘chirildi"
        return "Siz bu fanga yozilmagansiz"

    def get_info(self):
        asosiy = super().get_info()
        fakultet = f", Fakultet: {self.fakultet}" if self.fakultet else ""
        fanlar = ", ".join(f.get_info() for f in self.fanlar) or "Fanlar yo‘q"
        return f"{asosiy}{fakultet}. Fanlar: {fanlar}"


class Professor(Shaxs):
    def init(self, ism, yosh=None, kafedra=None):
        super().init(ism, yosh)
        self.kafedra = kafedra

    def dars_beradi(self, fan: Fan):
        return f"Professor {self.ism} {fan.nomi} fanidan dars bermoqda"

    def get_info(self):
        asosiy = super().get_info()
        return f"{asosiy}, Kafedra: {self.kafedra}"


class Foydalanuvchi(Shaxs):
    def init(self, ism, yosh=None, email=None):
        super().init(ism, yosh)
        self.email = email
        self.bloklangan = False

    def tizimga_kirish(self):
        if self.bloklangan:
            return "Foydalanuvchi bloklangan"
        return f"{self.ism} tizimga kirdi"

    def get_info(self):
        asosiy = super().get_info()
        return f"{asosiy}, Email: {self.email}, Bloklangan: {self.bloklangan}"


class Sotuvchi(Shaxs):
    def init(self, ism, yosh=None, dokon_nomi=None):
        super().init(ism, yosh)
        self.dokon_nomi = dokon_nomi
        self.tovarlar = []

