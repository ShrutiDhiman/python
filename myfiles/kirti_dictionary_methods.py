print('####################	P y t h o n 	 D i c t i o n a r y 	  ####################')	          
print('___________________________________________________________________________________')
print(' ')
print("dict={'name':'Kirti','age':22}")
dict={'name':'Kirti','age':22}
print(dict)
print(' ')
print('___________________________________________________________________________________')
print("x=dict['age'] - accessing a particular item from dictionary")
x=dict['age']
print(x)
print(' ')
print('___________________________________________________________________________________')
print("x=dict.get('age') - accessing a item using get()")
x=dict.get('age')
print(x)
print('___________________________________________________________________________________')
print("dict['age']=25 - changing the values from the dictionary....from 21 to 22 ")
dict['age']=25
print(dict)
print(' ')
print('___________________________________________________________________________________')
print('showing the keys using for loop')
for i in dict:
	print(i)
print(' ')
print('___________________________________________________________________________________')

print('showing the values of the dictionary')
for i in dict:
	print(dict[i])
print(' ')
print("___________________________________________________________________________________")
print('showing the values using values()')
for i in dict.values():
	print(i)
print(' ')
print('___________________________________________________________________________________')
print('showing both keys and values using loop')
for x,y in dict.items():
	print(x,y)
print(' ')
print('___________________________________________________________________________________')
print('to check whether the key is present in the dictionary or not')
if 'name' in dict:
	print("Yes, 'name' is one of the keys in the dict dictionary")
print(' ')
print('___________________________________________________________________________________')
print('len(dict) - length of the dictionary')
print(len(dict))
print(' ')
print('___________________________________________________________________________________')
print("dict['place']='Jaipur' - adding items")
dict['place']='Jaipur'
print(dict)
print(' ')
print('___________________________________________________________________________________')
print("dict.pop('place') - removing items using pop")
dict.pop('place')
print(dict)
print(' ')
print('___________________________________________________________________________________')

# note that keywords are not string literals
# note the use of equals rather than colon for the assignment

print("x = dict.copy() - copying the dict")
x = dict.copy()
print(x)
print(' ')
print('___________________________________________________________________________________')

print("x = dict.setdefault('age', 35) - showing the default value")
x = dict.setdefault('age', 35)
print(x)
print(' ')
print('___________________________________________________________________________________')
print("dict.clear() - use to clear all data of dictionary")
dict.clear()
print (dict)
print(' ')
print('___________________________________________________________________________________')