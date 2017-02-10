print('03\tWPP to enter value in centimetre and convert it to meter and kilometre')
cm=float(input('enter the length in centimetres'))
print(str(cm)+' centimetres is '+str(float(cm/100))+' metres')
print(str(cm)+' centimetres is %.4f kilometres' %(cm/100000))
