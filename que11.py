print('11\tWPP to enter principal amount, time and interst rate. create a compound_interest(principal,time,rate) function to calculate compound interest')
def compound_interest(p,t,r,n):
    return (p*(1+float(r)/(100*n))**(n*t))
p=input('enter the principal money')
r=input('enter the annual nominal rate of interest')
t=input('enter the time in years')
n=input('enter the number of times the interest is compounded per year')
print('COMPOUND INTEREST: %.2f\ntherefore, total amount is %.2f'%((compound_interest(p,t,r,n)-p),compound_interest(p,t,r,n)))
