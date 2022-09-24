print("...................................................")
num = int(input("enter your loop: "))
numtotal = []
for i in range(num):
    data=int(input("enter your number: "))
    numtotal += [data]
print(numtotal)
numtotal.sort()
print(numtotal)
print("Lowest number is:", min(numtotal))
print("Highest number is:", max(numtotal))
print("...................................................")