menu = {
"Burger": 180000,
"Pizza": 250000,
"Sandwich": 120000,
"Drink": 40000
}

name = input(" Name : ")
purch = input(" purchase : ")
Number_of_purchases=int(input(" number of purchases :  "))

total = 0
if purch in (menu) :
    total = menu[purch] *Number_of_purchases
    print(f"مبلغ کل :{total}")
    if total > 500000 :
        discount = total * 10/100
        total = total - discount
        print(f"مبلغ نهایی با تخفیف :{total} ")
else :
    print(" Sorry,we do not have purch")

def your_purchase() :
    print(f" your name is: {name} .")
    print(f" purchase : {purch} .")
    print(f"quanity : {Number_of_purchases} . ")

your_purchase()