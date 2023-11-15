def CalculateBMI(height,kilogram):
    result = kilogram/((height/100)*(height/100))
    return result
def CalculateAVG(a,b):
    return (a+b)//2
def CalculateStair(n):
    if(n==1 or n==0):
        return 1
    elif(n>1):
        return CalculateStair(n-1)+CalculateStair(n-2)

def main():
    print(CalculateBMI(170,65))
    print(CalculateAVG(5,17))
    print("我也是個廣東人，所以我們可能是老鄉"+str(CalculateStair(4)))
    print("測試")

main()