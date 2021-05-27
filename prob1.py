str1=input("Enter a string: ")
s1=str1[0:2]
s2=str1[-2:]
s3=s1+s2
if len(str1)>2:
  print(s3)
else:
  print("Empty string")