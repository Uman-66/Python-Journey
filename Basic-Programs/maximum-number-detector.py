number_list=input("Enter your numbers ,seperated by spaces only").split()
for n in range(0 , len(number_list)):
    number_list[n]=int(number_list[n])
max_number = number_list[0]
for number in number_list:
    if max_number<number:
        max_number=number
print(f"Your greatest number of all these is {max_number}")