word=str(input("Input name here>> ")).title()

for i in word:
    if i.isupper() and "-" in word:
        print(i, end="")

