lst = [ ]
n = int(input("Enter number of elements : "))
  
for i in range(0, n):
  ele = input()
  lst.append(ele)

print(list(set(lst)))



