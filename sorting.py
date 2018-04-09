a_list=["AAA","Abc","BBB","Bca","ccc"]
a_list.sort(key=str.lower, reverse=True)
b_list=sorted(a_list)
print(a_list)
print(b_list)