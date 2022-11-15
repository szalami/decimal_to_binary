
def setVal(num):
    temp = 0
    while pow(2, temp) <= num:          
        temp = temp + 1
    return pow(2, temp-1)
        

num = int(input("Szám: "))

max = setVal(num)


while max >= 1: 
    if num >= max:
        print(1, end=" ")
        num = num - max
    else:
        print(0, end=" ")        
    max = max / 2

