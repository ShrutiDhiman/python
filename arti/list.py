list=['arti',20,0.3]
print(' ')
print('-----------------------------------------')
print('Current list is {0}.format(list)')

print('First element {0}, second element {1}, third element {2} from the list {3} '.format(list[0], list[1], list[2], list))
print(' ')
print('-----------------------------------------')

print('Last element {0}, second last element {1}, third last element {2} from the list {3} '.format(list[-1], list[-2], list[-3], list))
print(' ')
print('-----------------------------------------')

list[2]=1997
print('changing the 3rd element of the list {0}'.format(list))
print(' ')
print('-----------------------------------------')

print('printing the whole list=')
for i in list:
	print (i)
print(' ')
print('-----------------------------------------')
if 'arti' in list:
	print("checking whether the element 'arti' is present in the list or not=yes")
print(' ')
print('-----------------------------------------')
print('the length of the list is:')
print(len(list))
print(' ')
print('-----------------------------------------')
list.append(3)
print('adding one more element in the list')
print(list)
print(' ')
print('-----------------------------------------')
list.remove(3)
print('removing the element frm the list')
print(list)
print(' ')
print('-----------------------------------------')
list.pop()
print('removing the last element from the list by using pop command')
print(list)
print(' ')
print('-----------------------------------------')
del list[1]
print('deleting the specified element from the list')
print(list)
print(' ')
print('-----------------------------------------')
x = list.copy()
print('copying the list:')
print(x)
print(' ')
print('-----------------------------------------')
list1=['apple',7]
list.extend(list1)
print('extending the list:')
print(list)
print(' ')
print('-----------------------------------------')
list.insert(1,20)
print('inserting the element on a specific position in the list')
print(list)
print(' ')
print('-----------------------------------------')
list.reverse()
print('reverse of the list=')
print(list)
print(' ')
print('-----------------------------------------')
list.clear()
print('clear the list')
print(list)
print(' ')
print('-----------------------------------------')
list=['W','A','P','H']
list2=[20,3,97,7]
list2.sort()
list.sort()
print('sorting the lists=')
print(list)
print(list2)
print(' ')
print('-----------------------------------------')
