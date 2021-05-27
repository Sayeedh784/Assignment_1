def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  
  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    print(str1)
  else:
    print(str1)
str1= input("Enter the String")
not_poor(str1)