limit=int(input("Write the number till what you want all even numbers"))
total = 0
for number in range(0 ,limit+1 ,2):
    total +=number
print(total)