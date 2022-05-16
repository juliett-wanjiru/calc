first = float(input("Enter first Number => "))
sec = float(input("Enter Second Number => "))
opr = str(input("Enter Operation (+, -, *, /) => "))
if opr == "+":
    total = first + sec
elif opr == "-":
    total = first - sec
elif opr == "*":
    total = first * sec
else:
    total = str("please Enter a valid operation")

print(total)
    
