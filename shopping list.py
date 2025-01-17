shop_list=[]
while True:
	i=input("Enter your items: ")
	shop_list.append(i)
	if i=='done':
		break
shop_list1=len(shop_list)
print(shop_list)
print(shop_list1)
shop_list2=shop_list[0:shop_list1-1]
print(shop_list2)