from datetime import datetime

date = input('PLease input date dd.mm.yyyy: ')  #input date
add = int(input('Please input amount days to add: '))  #input add days
d = datetime.strptime(date,'%d.%m.%Y')  #convert string to date
t = d.timestamp()+add*24*3600   #convert date to stamp format and add days in stamp format
r = datetime.fromtimestamp(t)   #convert stamp format to date
print(r.strftime('%d.%m.%Y'))   #output result
