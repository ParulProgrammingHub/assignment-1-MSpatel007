print('05\tWPP to enter value in days and convert it to in form of years, month and days(assuming that all month has 30 days and year is of 360)')
days=input('enter the days')
years=days/360
temp=days%360
months=temp/30
rdays=temp%30
print(str(days)+' days is '+str(years)+' years, '+str(months)+' months and '+str(rdays)+' days')
