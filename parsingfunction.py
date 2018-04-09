items=["Aman",1,2,3]
list_str=[]
list_int=[]

def parse_list(abc):
	for x in items: 
		if isinstance(x, int) or isinstance(x, float):
			list_int.append(x)
		elif isinstance(x, str):
			list_str.append(x)
	else:
			pass
	return list_str, list_int		


print(parse_list(items))

