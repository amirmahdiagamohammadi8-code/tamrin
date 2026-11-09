class BankAccount:
    def __init__(self, name, shomare, mojodi):
        self.name = name
        self.shomare = shomare
        self.mojodi = mojodi

    def save_transaction(self, matn):
        with open("transactions.txt", "a", encoding="utf-8") as file:
            file.write(matn + "\n")

    def deposit(self, mablagh):
        if not isinstance(mablagh, (int, float)) or mablagh <= 0:
            print("مبلغ نامعتبر است")
        else:
            self.mojodi += mablagh
            print("واریز انجام شد")
            self.save_transaction(f"{self.name} واریز: {mablagh}")

    def withdraw(self, mablagh):
        if not isinstance(mablagh, (int, float)) or mablagh <= 0:
            print("مبلغ نامعتبر است")

        elif mablagh > self.mojodi:
            print("موجودی کافی نیست")

        else:
            self.mojodi -= mablagh
            print("برداشت انجام شد")
            self.save_transaction(f"{self.name} برداشت: {mablagh}")

    def show_balance(self):
        print(f"موجودی حساب {self.name}: {self.mojodi}")

    def transfer(self, hesab, mablagh):
        if not isinstance(mablagh, (int, float)) or mablagh <= 0:
            print("مبلغ نامعتبر است")

        elif mablagh > self.mojodi:
            print("موجودی کافی نیست")

        elif not isinstance(hesab, BankAccount):
            print("حساب مقصد نامعتبر است")

        else:
            self.mojodi -= mablagh
            hesab.mojodi += mablagh
            print("انتقال انجام شد")

            self.save_transaction(
                f"{self.name} انتقال داد {mablagh} به {hesab.name}"
            )


hesab1 = BankAccount("Ali", 1234, 500000)
hesab2 = BankAccount("Sara", 5678, 300000)

hesab1.deposit(100000)
hesab1.withdraw(50000)
hesab1.transfer(hesab2, 200000)

hesab1.show_balance()
hesab2.show_balance()