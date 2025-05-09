print "Welcome to the Calc Game-2025/APRIL at GURGAON"
calc=input("Please enter the digits and operator for calculation: ")
num1='0'
num2='0'
flag='Gotonum1'
for a in calc:
  if a in ['0','1','2','3','4','5','6','7','8','9']:
      if flag=='Gotonum1':
             num1= num1 + str(a)
      else:
             num2=num2+str(a)
  elif a in ['+', '-', '*', '/']:
        operator=a
        flag='Gotonum2'
        continue
print (num1) 
print (num2)
if  operator == '+': print (int(num1) + int(num2))
elif operator == '-': print (int(num1) - int(num2))
elif operator == '*': print (int(num1) * int(num2))
elif operator == '/': print (int(num1) / int(num2))
else: print('You have selected an invalid operator, please select +, -, * or / only')