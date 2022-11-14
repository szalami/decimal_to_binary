
max = 128
num = int(input("Szám: "))

while max >= 1:
    if (num >= max):
        print(1, end=" ")
        num = num - max
    else:
        print(0, end=" ")        
    max = max / 2

