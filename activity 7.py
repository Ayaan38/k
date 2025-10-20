lst = ['Apple','Guvava', 'Mango', 'Banana', 'Strawberry']
print("Length of list:", len(lst))
print("First element:", lst[0])
print("Last element:", lst[-1])
lst.append('Cherrie')
print("Updated list:", lst)
lst.remove('Guvava')
print("Updated list:", lst)
lst.sort()
print("Sorted list:", lst)
lst.pop(1)
print("Updated list:", 1)
lst.reverse()
print("Reversed list:", lst)
print("Multiplication on list:", lst*2)
lst = lst[:4]
print("Sliced list:", lst)
lst.clear()
print("Updated list:", lst)

my_dict = {}
my_dict = {1 :'Apple', 2 :'Banana'}
my_dict = {'Name':'Ayaan', 1:[2, 7, 1, 1]}
my_dict = {'Name':'Ayaan', 'age':'17'}
print(my_dict['Name'])
print(my_dict.get('age'))
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Islamabad'
print(my_dict)
print("Address: ", my_dict.get('address'))
my_dict.clear()
print(my_dict)