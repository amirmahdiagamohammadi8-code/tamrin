inventory = {
"Laptop": 5,
 "Mouse": 20,
 "Keyboard": 12,
 "Monitor": 8
}
def append(mahsool, tedad):
    if mahsool in inventory:
        inventory[mahsool] += tedad
    else:
        inventory[mahsool] = tedad

    print(inventory)


def remove(mahsool, tedad):
    if mahsool in inventory:
        if tedad <= inventory[mahsool]:
            inventory[mahsool] -= tedad
            print(inventory)
        else:
            print("موجودی کافی نیست")
    else:
        print(f"sorry, we do not have {mahsool}")

for i in inventory :
        if inventory[i] < 5 :
           print(i)

products = set()

for i in inventory:
    products.add(i)

print(products)

def report():
    print("گزارش نهایی :")
    for i in inventory:
        print(f"{i}: {inventory[i]}")

report()

append("Mouse", 3)
remove("Keyboard", 2)