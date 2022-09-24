A = int(input("คะเเนนเก็บ : "))
B = int(input("คะเเนนสอบกลางงภาค : "))
C = int(input("คะเเนนสอบปลายภาค : "))
D = A+B+C

if D >= 80 :
    print("A")
elif D >= 75 :
    print("B+")
elif D >= 70 :
    print("B")
elif D >= 65 :
    print("C+")
elif D >= 55 :
    print("D+")
elif D >= 50 :
    print("D")
elif D >= 0 :
    print("F")