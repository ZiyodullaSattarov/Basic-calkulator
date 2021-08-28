a = int(input("1-Sonni kiriting:  "))
b = input("Amalni tanlang: |(+, -, *, / )|  ")
c = int(input("2-Sonni kiriting:  "))

if b == "+":
    print( a+  c)
elif b == "-":
    print(a - c)    
elif b == "*":
    print(a * c)    
elif b == "/":
    print(a / c)    
else:
    print("Nimadir not'g'ri ketdi...")