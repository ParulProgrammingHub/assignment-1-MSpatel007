print('09\tWPP to enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage. if percentage is less than 35 print fail else print pass')
sum=0
print('enter marks out of 100')
for i in range(5):
    sum=float(sum+input('enter marks of subject %s'%(i+1)))
mean=float(sum/5);
percent=float((sum/500)*100)
print('MEAN is %.2f\nPERCENTAGE is %.2f'%(mean,percent))
if(percent<35):print('FAIL')
else:print('PASS')
