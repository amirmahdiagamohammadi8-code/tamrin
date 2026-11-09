class Course:
    def __init__(self, name, ostad, zarfiat):
        self.name = name
        self.ostad = ostad
        self.zarfiat = zarfiat
        self.daneshjo = []

    def register_student(self, daneshjo):
        if daneshjo in self.daneshjo:
            print("این دانشجو قبلاً ثبت نام شده")

        elif len(self.daneshjo) < self.zarfiat:
            self.daneshjo.append(daneshjo)
            print("ثبت نام انجام شد")

        else:
            print("ظرفیت دوره تکمیل است")

    def remove_student(self, daneshjo):
        if daneshjo in self.daneshjo:
            self.daneshjo.remove(daneshjo)
            print("دانشجو حذف شد")
        else:
            print("دانشجو پیدا نشد")

    def show_students(self):
        print(self.daneshjo)

    def remaining_capacity(self):
        print(self.zarfiat - len(self.daneshjo))

    def __str__(self):
        return f"نام دوره: {self.name} | استاد: {self.ostad} | ظرفیت: {self.zarfiat}"


course1 = Course("Python", "Ali", 3)
course2 = Course("Java", "Reza", 5)

course1.register_student("Sara")
course1.register_student("Amir")

print(course1)
course1.show_students()
course1.remaining_capacity()