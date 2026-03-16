w = float(input())
h = float(input())

b = w / (h * h)

if b > 25:
    print("Overweight")
elif 18.5 <= b <= 25.0:
    print("Normal weight")
else:
    print("Underweight")