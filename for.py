a=8
b=9
if a > b:
  print('a is greater that b')
else:
  print('a is smaller than b')


loc='Bank'

if loc == 'Autoshop':
	print('Cars are cool')
elif loc=='Bank':
	print('Money is cool')
else:
	print('I dont understand')

items=[1,2,3,4]
for i in items:
	print(i)

my_list=[1,2,3,4,5,6,7,8,9,10]
print('Hello 1st number is')
for num in my_list:
	print(num)
	print('next number is')


for num in my_list:
 	if num%2 == 0:            #print even number
 		print(num)
 	else:
 		print('odd number:', num)     # it can be written as print(f'odd number: {num}')


my_string='Hello World'       #using strings
for letter in my_string:
	print(letter)


tup=(1,2,3)                # using tuples
for item in tup:
	print(item)



my_data=[(1,2),(3,4),(5,6),(7,8)]
len(my_data)

for item in my_data:
	print(item)


#tuple unpacking
for a,b in my_data:           #it can be written as for (a,b) in my_data:
	print(a)
	print(b)

d= {'k1':1,'k2':2,'k3':3}     
for x in d:                    #it displays only K1,k2,k3
	print(x)

d= {'k1':1,'k2':2,'k3':3}         
for x in d.items():                  #it displays keys and values ie.,d= {'k1':1,'k2':2,'k3':3}
	print(x)


for a,b in d.items():            #it prints only values ie.,1 , 2,and 3   (replace b with a it gives key)
	print(b)


for val in d.values():            #if you only need values - it prints only values ie.,1 , 2,and 3   
	print(val)
