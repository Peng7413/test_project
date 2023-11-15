def CalculateBMI(height,kilogram):
    result = kilogram/((height/100)*(height/100))
    print('BMI:%d' %result)
    return result
def CalculateAVG(a,b):
    print('%d %d' %(a,b))
    return (a+b)//2
def CalculateStair(n):
    print('%d' %n)
    return 0

def main():
    CalculateBMI(170,65)
    CalculateAVG(5,17)
    CalculateStair(8)
    print("測試")

main()