''' Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: 
Consider use range(#begin, #end) method
'''

# Solution
list = []
for i in range(10):
    if (i % 2 == 0) and (i % 3 != 0):
        list.append(i)
print(list, sep=',')

''' Question 2

Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
'''
# Solution
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)
x = int(input('Enter a number: '))
print(fact(x))

''' Question 3

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()
'''
n = int(input('Enter a number: '))
d = dict()
for i in range(1, n+1):
    d[i] = i * i
print(d)

''' Question 4

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple
'''
num = input('Enter values: ')
l = num.split(',')
t = tuple(l)
print(l)
print(t)

# Question

# What are the contents of lst after the following assignment?

lst = ([(x, y) for y in range(3) if x<y] for x in range(3))

for i in lst:
    print(i)
# Question
# What is the output of the following code snippet?

d = {}
for x in range(10):
    if x/2 in d:
        d[x/2] += x
    d[x] = 0

print(d[1], d[2])

# Question
# What is the output of the following code snippet?

d = {i: [] for i in range(10)}
for a in range(10):
    for b in range(10):
        d[a].append(a*b)
print(d[3])

# Question
# What is the output of the following code snippet?

def func(x, y, z=10):
    return x + y + z
print(func(1, 2, 3))

# Question

# What are the contents of lst after the following assignment?

lst = [(s, len(s)) for s in ('apple', 'banana', 'fish')]

# Question
# What are the contents of lst after the following assignment?



'''
Question:

By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:

li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print li
'''

lst = [12, 24, 35, 70, 88, 120, 155]
lst = [x for (i, x) in enumerate(lst) if i not in (0, 4, 5)]

'''
uestion:

By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.
'''
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)



# Given the following variable definitions:
lst1 = ['x', 'y', 'z']
lst2 = ['<', '>']
nums = (2, 3, 5, 7)
suffixes = ('ed', 'ish', 'e')
sentence = 'red fish yellow whale'
words    = sentence.split()

# Choose the value of the object assigned to x at 
# the end of each of the following snippets of code.
x = sum(i for i in range(10) if i not in nums)


x = [a+b+a for a in lst1 for b in lst2]

x = [[b+a+b for a in lst1] for b in lst2]


result = {}
for i in range(5):
    for j in range(10):
        result[i] = j

lst = list(range(10))
lst[1:8] = [2*x+1 for x in range(1, 4)]

# What are the contents of lst2 after the following two statements are carried out?
lst1 = [x*x for x in range(1, 5)]
lst2 = [y-1 for y in lst1 if y % 3 == 0]

# What is the output of the following code snippet?
x = 0
for i in range(100):    
    if i % 9 == 0:        
        x = i
    
    else:    
        x = -1
print(x)

# What are the contents of the listlstafter the following code is executed?

lst = [2*x+y for x in range(3) for y in range(3,6)]

# What are the contents of the list lst after the following code is executed?

lst = [(x,2**x) for x in range(1,8,2)]

# What are the contents of the dictionary dct after the following code is executed?
dct = {}
for x in 'a man a plan a canal'.split():
    if len(x) not in dct:
        dct[len(x)] = [x]
    else:
        dct[len(x)].append(x)


# What are the contents of the dictionary dct after the following code is executed?
dct = {}
for x in range(4, 21, 4):
    dct[x/4] = x*2

# What does the following list comprehension evaluate to?

[x+y for x in range(1,4) for y in range(2,6) if x < y]

result = []
for s in 'hello how are you'.split():

    result.insert(0, s)