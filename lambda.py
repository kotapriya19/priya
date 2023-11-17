##1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda
##function that multiplies argument x with argument y and prints the result.
##Sample Output:
##25
##48
'''
list=lambda x:x+15
print(list(10))

output:
25
'''
#------------
'''list=lambda x,y:x*y
print(list(6,8))

output:
48
'''

#===============================
##2. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
##Sample Output:
##Double the number of 15 = 30
##Triple the number of 15 = 45
##Quadruple the number of 15 = 60
##Quintuple the number 15 = 75

'''list=lambda x:x*2
print('double',list(15))
list=lambda x:x*3
print('triple',list(15))
list=lambda x:x*4
print('quadruple',list(15))
list=lambda x:x*5
print('quintuple',list(15))

output:
double 30
triple 45
quadruple 60
quintuple 75'''

#-----------------------

'''def fun(n):
    return lambda x:x*n
result=fun(2)
print("double",result(15))
result=fun(3)
print("triple",result(15))
result=fun(4)
print("quadruple",result(15))
result=fun(5)
print("quintuple",result(15))

output:
double 30
triple 45
quadruple 60
quintuple 75'''

#===============================
##3. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

'''
list=[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
res=sorted(list,key=lambda x:x[1])
print(res)

output:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]'''

#=============================================

##4. Write a Python program to sort a list of dictionaries using Lambda.
##Original list of dictionaries :
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
##{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
##Sorting the List of dictionaries :
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
##{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]


'''original=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

res=sorted(original,key=lambda x:x['color'])
print(res)

output:
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

#================================================

##5. Write a Python program to filter a list of integers using Lambda.
##Original list of integers:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##Even numbers from the said list:
##[2, 4, 6, 8, 10]
##Odd numbers from the said list:
##[1, 3, 5, 7, 9]


'''original=[1,2,3,4,5,6,7,8,9,10]
res=list(filter(lambda x: x%2==0,original))
print("even numbers",res)
res=list(filter(lambda x:x%2!=0,original))
print("odd numbers",res)

output:
even numbers [2, 4, 6, 8, 10]
odd numbers [1, 3, 5, 7, 9]'''

#-------------------
##6. Write a Python program to square and cube every number in a given list of integers using Lambda.
##Original list of integers:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##Square every number of the said list:
##[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##Cube every number of the said list:
##[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''original=[1,2,3,4,5,6,7,8,9,10]
res=list(map(lambda x:x**2,original))
print("square of numbers",res)
res=list(map(lambda x:x**3,original))
print("cube of numbers",res)

output:
square of numbers [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cube of numbers [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
'''

#=====================================
##7. Write a Python program to find if a given string starts with a given character using Lambda.
##Sample Output:
##True
##False

##string="given character using Lambda"
##res=lambda x:True if string.startswith('g') else False
##print(res("priy"))

'''res=lambda x:True if x.startswith('p') else False
print(res("priya"))

output:
True'''
#==================================================
##8. Write a Python program to extract year, month, date and time using Lambda.
##Sample Output:
##2020-01-15 09:03:32.744178
##2020
##1
##15
##09:03:32.744178

'''import datetime
now=datetime.datetime.now()
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
t=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))

output:
2023
5
9
18:00:58.871640
'''
#================================================
##9.Write a Python program to check whether a given string is a number or not using Lambda.

'''res=lambda q:q.replace('.','',1).isdigit()
print(res('3456'))
print(res('A001'))
print(res('4.678'))
print("\n print checking numberrr")
res1=lambda x:res(x[1:]) if x[0]=='-' else res(x)
print(res1('-756.23'))
print(res1('S3245'))

output:
True
False
True
True
False

'''
#=======================================
##10. Write a Python program to create Fibonacci series up to n using Lambda.

'''from functools import reduce
res=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
print(res(11))

output:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
'''
#=======================================
##11. Write a Python program to find the intersection of two given arrays using Lambda.
##Original arrays:
##[1, 2, 3, 5, 7, 8, 9, 10]
##[1, 2, 4, 8, 9]
##Intersection of the said arrays: [1, 2, 8, 9]

'''a=[1, 2, 3, 5, 7, 8, 9, 10]
b=[1, 2, 4, 8, 9]
res=list(filter(lambda x:x in a,b))
print("intersection of two lists:",res)

output:
intersection of two lists: [1, 2, 8, 9]'''
#=====================================
##12.Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
'''
list=[-1, 2, -3, 5, 7, 8, 9, -10]
res=sorted(list,key=lambda x:o if x==0 else -1/x)
print(res)

output:
[2, 5, 7, 8, 9, -10, -3, -1]
'''
#==================================
##13.Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

'''l=[1,2,3,4,5,6,7,8,9,10]
res=len(list(filter(lambda x:(x%2==0),l)))
print("even number count",res)
res=len(list(filter(lambda x:x%2!=0,l)))
print("odd number count",res)

output:
even number count 5
odd number count 5
'''

#=======================================
##14.Write a Python program to filter a given list to determine if the values in the list have a length of 6 using Lambda.
'''
a=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days= filter(lambda x: x if len(x)==6 else '', a)
for d in days:
    print(d)

output:
Monday
Friday
Sunday
'''
#==================================
##15.Write a Python program to add two given lists using map and lambda.
'''a=[2,3,4]
b=[6,7,8]
res=list(map(lambda x,y:x+y,a,b))
print(res)

output:
[8, 10, 12]'''

#============================
##16.'''prime number'''

'''input=list(filter(lambda x:all(x%i!=0 for i in range(2,int(x**0.5)+1)) and x>1, range(1,50)))
print(input)

output:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

'''
#===================================
##17.'''plaindrome '''
'''a=lambda x:x==x[::-1]
print(a('121'))

output:
True'''
#=====================================
##18.'''factorial number'''

'''fact=lambda x:1 if x==0 else x*fact(x-1)
print("the factorial number",fact(5))

output:
the factorial number 120
'''
#===============================
##19.'''armstrong number'''

'''n=int(input("enter a number"))
a=list(map(int,str(n)))
print(a)
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("it is an armstrong number")
else:
    print("not")


output:
enter a number153
[1, 5, 3]
it is an armstrong number
'''
#====================================
##20.'''find max values in list'''

'''input=[1,2,3,4,5,6,7]
input1=max(list(filter(lambda x:x,range(100))))
print("the maximum value in given list is:",input1)

output:
the maximum value in given list is: 99
'''
#========================================
#21.'''finding index position of list'''

'''a=['priya','purna','picky']
b=list(map(lambda x:(a.index(x),x),a))
print(b)

output:
[(0, 'priya'), (1, 'purna'), (2, 'picky')]
'''

#=================================
#22.'''finding length of string'''

'''input=lambda x:len(x)
print("The length of string is:",input('priya'))

output:
The length of string is: 5'''

#=========================
#23.basic string format

'''a=lambda s1,s2:f"{s1} {s2}"
print(a("priya","kota"))

output:
priya kota'''

#==========================
##24.fiding the sum and length

'''a=lambda x:sum(x)/len(x)
print(a([2,3,4,5,6,7]))

output:
4.5
'''
#===========================
##25.adding upper case to the string

'''a=["priya","kota","picky"]
b=list(map(lambda x:x.upper(),a))
print(b)

output:
['PRIYA', 'KOTA', 'PICKY']'''

#============

#how to add element in tuple

'''t=2,3,4
x=t+(5,5)
print(type(x))
'''
#==================
