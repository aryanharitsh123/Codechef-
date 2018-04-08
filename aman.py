match = 0
list_a=["Aryan","Aman",3525,50]
list_b=[]
for x in range(len(list_a)):
      x=x-match
      print(list_a[x])
      print(x)
      if isinstance(list_a[x], int):
          list_b.append(list_a[x])
          list_a.pop(x)
          match = match+1
print(list_a)
print(list_b)