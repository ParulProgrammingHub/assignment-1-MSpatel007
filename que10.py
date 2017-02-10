print('10\tWPP to enter principal amount, time and interst rate. create a simple_interest(principal,time,rate) function to calculate simple interest')
def simple_interest(principal,time,rate):
    return (principal*time*rate/100)
p=input('enter the principal money')
r=input('enter the rate of interest')
t=input('enter the time in years')
print('SIMPLE INTEREST: %.2f\ntherefore, total amount is %.2f'%(simple_interest(p,r,t),(simple_interest(p,r,t)+p)))
