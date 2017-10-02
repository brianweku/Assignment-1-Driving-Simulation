print("Enter numbers: ")
no1=int(input("1: "))
no2=int(input("2: "))
no3=int(input("3: "))
no4=int(input("4: "))
no5=int(input("5: "))
no6=int(input("6: "))
no7=int(input("7: "))
no8=int(input("8: "))
no9=int(input("9: "))
no0=int(input("10: "))
a=[no1, no2, no3, no4, no5, no6, no7, no8, no9, no0]
b=42
list=[]
for i in a:
    number=i%b
    list.append(number)
list1=set(list)
print(list)
print(len(list1))



