def CalculateBMI(height,kilogram):
    result = kilogram/((height/100)*(height/100))
    print('%d' %result)
    return 0
def CalculateAVG(a,b):
    result = (a+b)//2
    print('%d' %result)
    return result
def CalculateStair(n):
    result = 1
    for i in range(n):
        result *= (i+1)
    print('%d' %result)
    return result

def main():
    CalculateBMI(170,65)
    CalculateAVG(5,17)
    CalculateStair(8)
    print("測試")

main()