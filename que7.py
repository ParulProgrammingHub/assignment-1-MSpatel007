print('07\tWPP to enter 2 angles and using function thirdangle(angle1,angle2) calculate third angle')
def thirdangle(num1,num2):
    return (180-num1-num2)
angle1=input('enter angle1')
angle2=input('enter angle2')
print('the third angle is %.2f'%(float(thirdangle(angle1,angle2))))
