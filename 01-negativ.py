print("Add meg az első számot: ")
a = int(input())
print("Add meg a második számot: ")
b = int(input())

if a == 0 or b == 0:
    print("Adj meg egy nullától különböző számot!")
elif a > 0 and b > 0:
    print ("Egyik szám sem negatív.")
elif a < 0 and b > 0:
    print ("Az első szám negatív.")
elif a > 0 and b < 0:
    print("A második szám negatív.")
elif a < 0 and b < 0:
    print("Mindkét szám negatív.")
