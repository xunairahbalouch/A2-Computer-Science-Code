flag = False
count = 0
total = 0

while flag == False:
    num = float(input("enter the number:"))
    if num == 0:
     flag = True
else:
    count = count + 1
    total = total + num

average = total/count
print("Average is:", average)
