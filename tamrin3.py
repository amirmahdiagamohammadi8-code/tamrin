expenses = [ 
("Food", 250000),
 ("Transport", 80000), 
 ("Shopping", 450000), 
 ("Food", 150000), 
 ("Education", 300000)
]
total = 0
food = 0
Transport = 0
Shopping = 0
Education = 0
for i in expenses :
   total = total +i[1]

for i in expenses :

    if i[0] == "Food" :
      food = food + i[1]

    if i[0] == "Transport" :
       Transport = Transport + i[1]

    if i[0] == "Shopping" :
      Shopping = Shopping + i[1]

    if i[0] == "Education" :
      Education = Education + i[1]



khargha =[]
for i in expenses :
   khargha.append(i[1])

dasteh = set()
for i in expenses :
   dasteh.add(i[0])
print(dasteh)

for number, item in enumerate(expenses, start=1):
    print(number, item)

def moratab():
   print(f"  هزینه کل : {total}")
   print(f"غذا :{food}")
   print(f" رفت و امد :{Transport}")
   print(f" خرید :{Shopping}")
   print(f" اموزش :{Education}")
   print(max(khargha))
   
moratab()