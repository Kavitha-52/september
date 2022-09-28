
'''a=10
print(a)#10
print(type(a))#<class 'int'>

a=10.12234
print(a)#10.12234
print(type(a))#<class 'float'>

a='a'
print(a)#a
print(type(a))#<class 'str'>

a="hello"
print(a)#hello
print(type(a))#<class 'str'>

a=1+2j
print(a)#1+2j
print(type(a))#<class 'complex'>

a=complex(2,4)
print(a)#2+4j
print(type(a))#<class 'complex'>


#int a=10---invalid syntax
#float a=10.3345
#char a='x'
# char str="string" 

#123=100-->invalid cant start with integer
A=100
print(A)#100

_a=100
print(_a)#100

_a123=100
print(_a123)#100


##literals
intvar=100
print(intvar)

floatvar=10.78
print(floatvar)

complexvar=complex(1,2)
print(complexvar)

strvar="python"
print(strvar)

boolvar=True
print(boolvar)

nonevar=None
print(nonevar)

listvar=[1,2,3,4]
print(listvar)

tuplevar=(1,2,3)
print(tuplevar)

setvar={1,2,3}
print(setvar)

dicvar={1:"one",2:"two",3:"three"}
print(dicvar)

##multiple assignment

a=b=c= 10
print(a,b,c)# 10 10 10

a,b,c,d=10,10.12,'c',"hello"
print(a,b,c,d)#10 10.12 c hello
print(d,c,b,a)#hello c 10.12 10
print(b,d,a,c)#10.12 hello 10 c

#a=None=1-->cannot assign to none

##format() functions

name="my name is {fname},I am {age}years old".format(fname="jonny",age=2)
print(name)#my name is jonny,I am 2years old
                                                      

name="my name is {0},I am {1}years old".format("jonny",2)
print(name)#my name is jonny,I am 2years old

name="my name is {},I am {}years old.".format("jonny",2)
print(name)#my name is jonny,I am 2years old


##typecasting

a=10
b=20.5
c=a+b
print(c)#30.5-->implicit type


#explicit type

a=10
print(a)#10
print(float(a))#10.0
      
b=10.12
print(b)#10.12
print(int(b))#10


##id()
a=10
print(id(a))#2921071903248
b=10
print(id(b))#2921071903248

str="pthon"
print(id(str))#2780138756208

str="Python"
print(id(str))#2780102869872


x=3
print(id(x))#2168579227952

print(id(x+0))#2168579227952

print(id(x+1))#2168579227984

x=4
print(id(x-1))#2514532041008

x=4.0
print(id(x))#2514571813712


x=1
print(id(1))#2616861327600

x=2
print(id(2))#2616861327632

print(id(1)-id(2))#32
x=1
y=x
print(x is y)#true

print(x is not y)#false

x=1
y=2
print(x is  y)#false
print(x is not y)#true

x = 5
y = "John"
print(x)#5
print(y)#join

x=1
x="hello"
print(x)#hello

x=str(3)
y=int(3)
z=float(3)
print(x,y,z)

set1 = set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)


##functions


def f():
    print("hello")
f()



def f():
    s="hello"
    return s    
a=f()  
print(a)


def f1():
    for i in range(10):
        print("hii",end=" ")
f1()


def f1():
    s="python"
    for i in s:
        print(i,end=" ")
    
f1()

##fun with 1 parameter

def f(a):
    print(a+2)#4
f(2)

def f(a):
    print(a*2)#8
f(a=int(input("enter a number:")))#4

def f(a):
    print(a*2)# hii hii
f("hii ")

##fun with 2 parameters

def add(a,b):
    print("sum:",a+b)
add(2,6)


def add(a,b):
    return a+b    
x=add(2,6)
print("sum is:",x)


def add(a,b):
    print("sum:",a+b)
add(a=int(input("enter a value:")),b=int(input("enter b value")))



def check(a,b):
    if(a>b):
        print(a,"is greater")
    else:
        print(b,"is greater")
check(10,20)

def check(a,b,c):
    if(a>b and a>c):
        print(a,"is greater")
    elif(b>c):
        print(b,"is greater")
    else:
        print( c,"is gretaer")
check(10,20,30)

def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(10,20)
print("sum is:",x,"\nsub is :",y)


##functions with variables

def f1():
    a=10
    print(a)
    #print(b)
    
def f2():
    b=20
    print(b)
   # print(a)
f1()
f2()


a=10
def f1():
    print(a)
def f2():
    global a
    x=a+10
    print(a)
    print(x)
f1()
f2()

a=10
def f1():
    global a
    a=50
    print(a)#50
def f2():
    print(a)#50
f1()
f2()


a=10
def f1():
    global a
    a=50
    print(a)#50
def f2():
    print(a)#10
f2()
f1()


#positional arg

def sub(a,b):
    print("sub is :",a-b)
sub(1,2)#sub is : -1
sub(10,5)#sub is :5

#keyword arg

def sub(a,b):
    print("sub is :",a-b)
sub(a=1,b=2)#sub is : -1
sub(b=10,a=5)#sub is : -5

#default arg

def f(course):
    print("course is :",course)#course is : c
f("c")



def f(course):
    print("course is :",course)#course is : python
f("python")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



#variable length arg

def f1(*a):
    print(a)
f1(1)
f1(1,2)
f1(1,2,3)
f1(1,2,3,4)
f1("hii","how are u",2 ,'K')
#o/p:
#(1,)
#(1, 2)
#(1, 2, 3)
#(1, 2, 3, 4)
#('hii', 'how are u', 2, 'K')

#positional  only arg

def add(a,b):#normal method
    print("sum is:",a+b)
add(1,2)
add(a=10,b=20)

def add(a,b,/):#normal method
    print("sum is:",a+b)
add(1,2)
#add(a=10,b=20)-- type error
   

#keyword  only arg

def add(*,a,b):#normal method
    print("sum is:",a+b)
#add(1,2)-->type error positional arg
add(a=10,b=20)

#nested fun

def f1():
    print("welcome")
    def f2():
        print("thundersoft")
    f2()
f1()


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

def add(num1, num2) 
    """Add two numbers"""
    num3 = num1 + num2
 
    return num3
 
 
# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(ans)

def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
 
evenOdd(2)
evenOdd(3)

def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
 
myFun(10)

def myFun(*argv):
    for arg in argv:
        print(arg)
 
 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(first='Geeks', mid='for', last='Geeks')


def myFun(x):
    x[0] = 20
    print(lst)
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)



def swap(x, y):
    temp = x
    x = y
    y = temp
 
 
def swap(x,y):
    temp=x
    x=y
    y=temp
    print(x,y)
    
x = 2
y = 3
swap(x, y)
print(x)
print(y)


###Operators

#arithmetic

print(5+2)#7
print(5-2)#3
print(5*2)#10
print(5/2) #2.5   
print(5//2)#2
print(5%2)#1
print(5**2)#25
print(5+3-2)#6
print(5+3*2)#11
print((5+3)*2)#16



#Relational
print(5<2)#false
print(5>2)#true
print(5<=2)#false
print(5>=2)#true
print(5==2)#false
print(5!=2)#true
print(1==int(1.0000))#true 
print(3!=3.0)#false
print(None==True)#false
print(None==False)#false
print(1==True)#true
print(0==False)#true



#assignmemt

a=7
a+=3
print(a)#10

a-=3#10-3
print(a)#7

a*=3
print(a)#21

a**=3
print(a)#9261

a/=3
print(a)#3087.0

a%=3
print(a)#0.0

##logical
print((2<3 and 3<5))#true
print((2<3 and 5<3))#false
print((1>2 and 5<6))#false

print((2<3 or 3<5))#true
print((2<3 or 5<3))#true
print((1>2 or 5<6))#true
print((1>2 or 5>6))#true


print(not(3>5))#true
print(not(3<5))#false
print(not(3==5))#true
print(not(3!=5))#false

#membership

l=[1,2,3,4,5,6]
print(1 in l)#true
print(10 in l)#false
print(10 not in l)#true
print(2 not in l)#false

#identity

a=2
b=2
print(a is b)#true
print( a is not b)# false
print(id(a),id(b))#2273880441104 2273880441104

a=2
b=3
print(a is b)#false
print( a is not b)# true
print(id(a),id(b))#1415539589392 1415539589424

a="sai"
b="Sai"
print(a is b)#false
print( a is not b)# true
print(id(a),id(b))#1760788404336 1760788404464

a=[1,2,3]
b=[1,2,3]
c=a
print(a is c)#true
print(b is a)#false
print(id(a))#2657759595776
print(id(c))#2657759595776
print(id(b))#2657759595976

#bitwise operators
a=2
b=4
print(bin(a))#0b10
print(bin(b))#0b100

print(bin(a&b))#0b0
print(a&b)#0

print(bin(a|b))#0b110
print(a|b)#6

print(bin(a^b))#0b110
print(a^b)#6

a=8
print(a<<2)#32
print(a>>2)#2


##control statements

i=10
if i==10:
    print("True")#true

i=10
if i==10:
    print("true")#true
else:
    print("false")

i=int(input("enter a number:"))
j=int(input("enter a number:"))
if(i>j):
    print(i,"is greater")
else:
    print(j,"is greater")

    
i=int(input("enter a number:"))
if(i==1):
    print("one")
elif(i==2):
    print("two")
elif(i==3):
    print("three")
elif(i==4):
    print("four")
else:
    print("invalid")

a = 2
b = 330

print("A") if a > b else print("B")#B

fruits=["apple","banana","grapes","mango"]
for i in fruits:
    print(i)
#o/p:apple
#banana
#grapes
#mango

str="apple"
for i in str:
    print(i,end=" ")#a p p l e


    
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break#apple banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)#apple 

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)#apple cherry
  

for x in range(6):
  print(x,end=" ")#0 1 2 3 4 5

for x in range(6,0,-1):
    print(x,end=" ")# 6 5 4 3 2 1

for x in range(2, 30, 3):
  print(x,end=" ")#2 5 8 11 14 17 20 23 26 29

for x in range(6):
  if x == 3: break
  print(x,end=" ")# 0 1 2
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#o/p:red apple
#red banana
#red cherry
#big apple
#big banana
#big cherry
#tasty apple
#tasty banana
#tasty cherry

#while
i = 1
while i < 6:
  print(i,end=" ")#1 2 3 4 5
  i += 1


i = 1
while i < 6:
  print(i,end=" ")#1 2 3 
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i,end=" ")#1 2 4 5 6
         


s1="python"
print(s1)
print("s1=",id(s1))
s2="python"
print("s2=",id(s2))
s1=s1+s2 #immutable
print(s1)
print("s1=",id(s1))

o/p:
python
s1= 1317878573552
s2= 1317878573552
pythonpython
s1= 1317878747632

a='this 'python tutorial' is for you'

a="this "python tutorial" is for you"

# invalid syntax 

a="this 'python tutorial' is for you"
print(a)

a='this "python tutorial" is for you'
print(a)

#single quote within in double quotes is possible & vice verse


a= hiii hello
      how are you
print(a)
o/p:hiii hello
      how are you
      

a="""hiii hello
      how are you"""
print(a)
o/p:hiii hello
      how are you

##Escape sequences
s="thunder\'soft is in hyd"
print(s)
o/p:thunder'soft is in hyd

s="thunder\"soft is in hyd"
print(s)
o/p:thunder"soft is in hyd

s="python\\training"
print(s)
o/p:python\training

s="python\ntraining"
print(s)
o/p:python
    training

s="python\ttraining"
print(s)
o/p:python training
##format specifiers

str="python"
print("%s is easy to learn" %str)
o/p:python is easy to learn
#print("%s is easy to learn",%str)--> invalid syn


name="Honey"
age=3
print("%s age is %d years"%(name,age))
#o/p:Honey age is 3 years

name="Honey"
age=3.12345
print("%s age is %d years"%(name,age))
#o/p:Honey age is 3 years

name="Honey"
age=3
print("%s age is %f years"%(name,age))
#o/p:Honey age is 3.000000 years




name="sai"
print("my name  is ",name)
print("my name  is %s"%name)
o/p:my name  is  sai

name=input("enter your name:")
print("your name is :",name)
o/p:my name  is  sai

#indexing
s="python"
print("s[0]:",s[0])
print("s[1]:",s[1])
print("s[2]:",s[2])
print("s[3]:",s[3])
print("s[4]:",s[4])
print("s[5]:",s[5])
#print("s[6]:",s[6])-->index error
o/p:s[0]: p
s[1]: y
s[2]: t
s[3]: h
s[4]: o
s[5]: n
#using for
x=0
for i in s:
    print("s[%d]:"%x,i)
    x=x+1

o/p:
s[0]: p
s[1]: y
s[2]: t
s[3]: h
s[4]: o
s[5]: n

#slicing
s="thundersoft"
print(s[:])#thundersoft
print(s[:7])#thunder
print(s[7:11])#soft
print(s[0:11:2])#tudrot
print(s[:-1])#thundersof
print(s[-10:-5])#hunde
print(s[::-1])#tfosrednuht

#capitalize--> it gives only 1st word capital 
s="python is  very easy"
print(s.capitalize())
#o/p:Python is  very easy
s="Python Is  Very Easy"
print(s.capitalize())
#o/p:Python is  very easy

#Title-->it gives every word 1st letter is capital

s="python is  very easy"
print(s.title())    
#o/p:Python Is  Very Easy

s="Python is  Very easy"
s1=s.title()
print(s1)
#o/p:Python Is  Very Easy

s="Python is  Very easy"
s.title()
print(s)
#o/p:Python is  Very easy

##upper()
s="thundersoft"
print(s.upper())
#o/p:THUNDERSOFT

##lower()
s="THUNDERSOFT"
print(s.lower())
#o/p:thundersoft

##swapcase()
s="tHUNDERsOFT"
print(s.swapcase())
#olp:ThunderSoft

##count()##
s="python is very is easy is"
print(s.count("is"))#3
print(s.count('is'))#3
print(s.count("e"))#2
print(s.count(" "))#5
print(s.count('e'))#2
print(s.count(e))#name error

##center()
s="python is easy"
new_str=s.center(30,'*')
print(new_str)
#o/p:********python is easy********

new_str=s.center(31,"*")
print(new_str)
#o/p:*********python is easy********

new_str=s.center(36,'*')
print(new_str)
#o/p:***********python is easy*********** 

##startswith() & endswith()
s="python is very easy"
print(s.startswith('p'))#True
s1=s.startswith('n')
print(s1)#False
print(s.startswith("python"))#True
print(s.endswith("python"))#False
print(s.endswith("easy"))#True
print(s.endswith("y"))#True
print(s.endswith("p"))#False
print(s.endswith("s"))#False

#expandtabs()
s="python\tlanguage"
print(s.expandtabs(5))#python    language
print(s.expandtabs(0))#pythonlanguage
print(s.expandtabs(10))#python    language
s="p\ty"
print(s.expandtabs(10))#p         y

s.expandtabs(2)
print(s)#p	y

s="p\tython"
x=s.expandtabs(10)
print(x)#p         ython

##find()-->it gives index of character
s="python is very  is easy"
print(s.find("is"))#7
print(s.find('y'))#1
x=s.find('y')
print(x)#1
print(s.find('z'))# it won't give error returns only -1

##rfind()
s="python is very is easy"
print(s.rfind("is"))#15
print(s.rfind('y'))#21
x=s.rfind('i',1)
print(x)#15
print(s.rfind('z'))#-1

##index-->
s="python is very  is easy"
print(s.index("is"))#7
print(s.index('y'))#1
x=s.index('y')
print(x)#1
print(s.index('z'))#it gives error,it is main diff

#rindex-->return highest index

s="python is very  is easy"
print(s.rindex("is"))#16
print(s.rindex("e"))#19
x=s.rindex('y')
print(x)#22
print(s.rindex('z'))#value error
##isdigit()

s="1234"
print(s.isdigit())#True
print(s.isdecimal())#True
s="12wert34"
print(s.isdigit())#False
s="qwerty"
print(s.isdigit())#True
s="12 34"
print(s.isdigit())#False

##isalpha

s="acvbn"
print(s.isalpha())#True
s=" "
print(s.isalpha())#false
s="a"
print(s.isalpha())#true
s="acv12bn"
print(s.isalpha())#False
s="acv bn"
print(s.isalpha())#True
s="2345"
s1=s.isalpha()
print(s1)#False

##isalnum
s="132wqerty"
print(s.isalnum())#True

s="13212234"
print(s.isalnum())#True

s="qwertyu"
print(s.isalnum())#True

s="132 weert"
print(s.isalnum())#false

s="assd fghj"
print(s.isalnum())#False

##isidentifier()
s="python"
print(s.isidentifier())#True

s="pyt hon"
print(s.isidentifier())#False

s="df12345"
print(s.isidentifier())#True

s="12345"
print(s.isidentifier())#False

s="1223 456"
print(s.isidentifier())#False

##isnumeric()
s="1/2"
print(s.isnumeric())#False

s="4/2"
print(s.isnumeric())#False

s="123"
print(s.isnumeric())#True

s="123.234"
print(s.isnumeric())#False

s="sdfgh"
print(s.isnumeric())#False

s="12312sdf"
print(s.isnumeric())#False

##isprintable()
s="python is very easy"
print(s.isprintable())#True

s=" "
print(s.isprintable())#True

s="python is very easy\n"
print(s.isprintable())#False

s="python\ is very easy"
print(s.isprintable())#True

s="python\t is very easy"
print(s.isprintable())#False

##isspace()
s=" "
print(s.isspace())#True

s=" \t"
print(s.isspace())#True

s="\t"
print(s.isspace())#True

s="qwerty"
print(s.isspace())#False

s="12234\t"
print(s.isspace())#False

s="qwe rty"
print(s.isspace())#False

s="122 34"
print(s.isspace())#False

##isjoin()
s1="!"
s2="welcome"
print(s1.join(s2))#w!e!l!c!o!m!e

s1="*"
s2="welcome"
print(s1.join(s2))#w*e*l*c*o*m*e

s1="10"
s2="welcome"
print(s1.join(s2))#w10e10l10c10o10m10e

s1="Hii"
s2="welcome"
print(s1.join(s2))#wHiieHiilHiicHiioHiimHiie
print("  ".join("sai"))#s  a  i
print(":".join("sai"))#s:a:i
print(" @".join("sai"))#s @a @i

##ljust()
s="python"
print(s.ljust(10,"*"))#python****
print(s.ljust(20,"*"))#python**************
print(s.ljust(5,"*"))#python

#rjust()
s="python"
print(s.rjust(10,"*"))#****python
print(s.rjust(20,"*"))#**************python
print(s.rjust(15,"*"))#*********python
print(s.rjust(15,"@"))#@@@@@@@@@python

##strip
s="   python   "
print(s)#   python 
print(s.strip())#python
print(s.lstrip())#python->left side space removed
print(s.rstrip())#   python->right side removed

##s.partition()-->it act as seperator
s="python is easy  language is easy"
print(s.partition('is'))#('python ', 'is', ' easy  language is easy')
print(s.partition('a'))#('python is e', 'a', 'sy  language is easy')
s1=s.partition('y')
print(s1)#('p', 'y', 'thon is easy  language is easy')
print(s.partition('x'))#('python is easy  language is easy', '', '')

#s.rpartition()
s="python is easy  language is easy"
print(s.rpartition('is'))#('python is easy  language ', 'is', ' easy')
print(s.rpartition('a'))#('python is easy  language is e', 'a', 'sy')
s1=s.rpartition('y')
print(s1)#('python is easy  language is eas', 'y', '')
print(s.rpartition('x'))#('', '', 'python is easy  language is easy')


##replace()

s="python is easy"
print(s.replace("python","java"))
#o/p:java is easy

s="sing sing sing sing sing"
print(s.replace("sing","song",2))
#o/p:song song sing sing sing

s="""python is easy
  python is easy
  python is easy"""
print(s.replace("python","java"))
#o/p:java is easy
     java is easy
     java is easy

##split()
s="python is very easy"
print(s.split())
#o/p:['python', 'is', 'very', 'easy']

s="python is very easy compared to ohter language"
print(s.split())
#o/p:['python', 'is', 'very', 'easy', 'compared', 'to', 'ohter', 'language']


##rsplit

s="apple,mango,pineapple,grapes"
print(s.rsplit(' ',0))
print(s.rsplit(' ',1))
print(s.rsplit(' ',2))
print(s.rsplit(' ',3))

##splitlines()
s="apple\nmango\npineapple\ngrapes"
print(s.splitlines())
#o/p:['apple', 'mango', 'pineapple', 'grapes']

s="apple\tmango\tpineapple\tgrapes"
print(s.splitlines())
#o/p:['apple\tmango\tpineapple\tgrapes']

s="apple,mango,pineapple,grapes"
print(s.splitlines())
#o/p:['apple,mango,pineapple,grapes']

#zfill()

s="python is easy"
print(s.zfill(18))
0000python is easy

s1=s.zfill(30)
print(s1)
#0000000000000000python is easy

print(s.zfill(10))
#python is easy


##isascii()
s="a"
print(s.isascii())#True
s="1"
print(s.isascii())#True
s="&"
print(s.isascii())#True

#format_map()
s={'x':9,'y':-7,'z':-2022}
print('{x}{y}{z}'.format_map(s))
#o/p:9-7-2022

s={'x':9,'y':/7,'z':/2022}
print('{x}{y}{z}'.format_map(s))#invalid



### set ###
s={}
print(s){}
print(type(s))#<class 'dict'>

s={1}
print(s)#{1}
print(type(s))#<class 'set'>

s={1,2,1.23,'K',"hii"}
print(s)
#o/p:{1, 2, 1.23, 'hii', 'K'}

s={1,2,1,2,1.23,'K',"hii"}
print(s)
#o/p:{1, 2, 1.23, 'hii', 'K'}

s={1,2,1,(2,1.23),'K',"hii"}
print(s)
#o/p:{1, 2, 'K', 'hii', (2, 1.23)}

s={1,2,1,[2,1.23],'K',"hii"}
print(s)
#o/p:type error

s={1,2,1,{2,1.23},'K',"hii"}
print(s)
#o/p:type error


s={1,2,1,2,1.23,'K',"hii"}
print(2 in s)#True
print('k' in s)#False
print("hii" in s)#True
print(20 in s)#False

x={1,2,3,4,5,'k',"apple"}
y={1,2,3,9,10,'s',"banana"}
print(x|y)
#o/p:{1, 2, 3, 4, 5, 's', 9, 10, 'k', 'banana', 'apple'}
print(x&y)#{1, 2, 3}-->common ele
print(x-y)#{'apple', 4, 5, 'k'}
print(y-x)#{'s', 'banana', 10, 9}
print(x^y)#{'apple', 'k', 4, 5, 's', 9, 10, 'banana'}

print(y^x)#{'apple', 'k', 4, 5, 's', 9, 10, 'banana'}
y={1,2,3,4,6,7,8}
x={1,2,3}
print(x<=y)#true
print(x>=y)#false

x={1,2,3,4,6,7,8}
y={1,2,3}
print(x<=y)#false
print(x>=y)#true

##add()

s={1,2,1,2,1.23,'K',"hii"}
s.add("python")
print(s)#{1, 2, 1.23, 'hii', 'K', 'python'}
s1=s.add("python")
print(s1)#None
print(s.add("pthon"))#None

##clear
s={1,2,1,2,1.23,'K',"hii"}
s.clear()
print(s)#set()

##copy->shallow copy -->diff memory location
s={1,2,1,2,1.23,'K',"hii"}
s1=s.copy()
print(s1)#{1, 'hii', 2, 1.23, 'K'}
print(id(s1))#2037078936928
print(id(s))#2037078937376
s.add("java")
print(s)#{1, 2, 1.23, 'K', 'hii', 'java'}
print(s1)#{1, 2, 1.23, 'K', 'hii'}


#deep copy-->s1 &s2 same memory loactions
s1={1,2,3}
s2=s1
print(s1)#{1, 2, 3}
print(s2)#{1, 2, 3}
print(id(s1),id(s2))#1445383884352 1445383884352
s1.add('k')
print(s1)#{1, 2, 3, 'k'}
print(s2)#{1, 2, 3, 'k'}
print(id(s1),id(s2))#1445383884352 1445383884352

#difference

a={1,2,3,4,5}
b={4,5,6,7,8}
print(a-b)#{1, 2, 3}
print(a.difference(b))#{1, 2, 3}
print(b.difference(a))#{8, 6, 7}

#discard
a={1,23,'q',"mango"}
b=a.discard("mango")
print(b)#none
print(a)#{1, 'q', 23}

#intersection
x={1,2,'k',"python",123}
y={3,2,'k',"Python",123}
print(x.intersection(y))#{2, 123, 'k'}
z=x.intersection(y)
print(z)#{2, 123, 'k'}

##isdisjoint()-->check interstion or not
x={1,2,'k',"python",123}
y={3,2,'k',"Python",123}
z=x.isdisjoint(y)
print(z)#false

x={1,2,'k',"python",123}
y={3,8,'a',"Python",18923}
z=x.isdisjoint(y)
print(z)#true

##issubset()

x={3,8,"Python"}
y={3,8,'a',"Python",18923}
print(x.issubset(y))#true
z=x.issubset(y)
print(z)#true

x={1,2,'k',"python",123}
y={3,8,'a',"Python",18923}
z=x.issubset(y)
print(z)#false

#issuperset()
x = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
y = {4, 3, 7, 8, 11}
print(x.issuperset(y))#true
print('x is Superset of y?',x >= y)#true
print('y is Superset of x?',y >= x)#false

x= {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
y = {4, 3, 7, 8, 11,67}
z=x.issuperset(y)
print(z)#false
print('x is Superset of y?',x >= y)#false
print('y is Superset of x?',y >= x)#false


##isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)#true

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)

print(result)#true

##pop()

s={1,2,3,4}
s.pop()
print(s)#{2, 3, 4}
print(s.pop())#2

fruits = {"apple", "banana", "cherry"}

x = fruits.pop()

print(x)#apple"
print(fruits)#{'banan','cherry'}

##remove()
s={1,2,3,4,5}
s.remove(1)
print(s)#{2, 3, 4, 5}
x=s.remove(4)
print(x)#none
print(s.remove(5))
print(s)#none
a={1,2,3,4,5,6}
b={5,6,7,8,9}
print(a.union(b))#{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a|b)#{1, 2, 3, 4, 5, 6, 7, 8, 9}

##update
s={1,"kavitha",'s'}
s.update(["sree","latha"])
print(s)#we can add any no of ele
#o/p:{'latha', 1, 'sree', 's', 'kavitha'

s.add([10,20,30])
print(s)#type error we can add only 1 ele


##symmtric_difference()
x={"c","c++","python"}
y={"c","c++","java"}
print(x.symmetric_difference(y))
#o/p:{'python', 'java'}

z=x.symmetric_difference(y)
print(z)
#o/p:{'python', 'java'}


##symmetric_difference_update()
x={"c","c++","python"}
y={"c","c++","java"}
print(x.symmetric_difference_update(y))

z=x.symmetric_difference_update(y)
print(z)

#all()
s={1,2,3,4,5,}
print(all(s))#true

s={1,2,3,4,5,0}
a=all(s)
print(a)#false

s={1,2,3,4,5,-7}
print(all(s))#true

##any()
s={0,0,0}
print(any(s))#false

s={1,0,0,0}
a=any(s)
print(a)#true

s={1,2,3,4,5,-7}
print(any(s))#true

##enumerate()
s={1,2,3,4,5,6,7,"hello"}
enumerate(s)
for i in s:
    print(i,end=" ")
#print(list(enumerate()))
#print(list(enumerate(s,100)))

##len()
s={1,2,3,4,"hii"}
print(len(s))#5

##list()
s={1,2,3,4,'d',"welcome"}
print(list(s))#[1, 2, 3, 4, 'd', 'welcome']

##max() , min()  & sum()
s={1,2,3,4,12,64}
print(max(s))#64

s={1,2,3,4,2433,45,-89,-1}
print(min(s))#=89

s={1,2,3,4,2433,45,-89,-1}
print(sum(s))#2398

##frozen set()->immutable-> set we can modify but in frozen set we cant modify
s={1,2,3,4,5}
fs=frozenset(s)
print(fs)#frozenset({1, 2, 3, 4, 5})
print(type(fs))#<class 'frozenset'>
print(type(s))#class 'set'>

x=frozenset({'a',12,'d'})
print(id(x))#2424872291456
y=x
print(id(y))#2424872291456
y|={1,2,3}
print(y)#frozenset({1, 2, 'd', 3, 'a', 12})
print(id(y))#2424872291904
print(x)#frozenset({'a', 'd', 12})
print(id(x))#2424872291456

###dictonary
d={}
print(d)#{}
print(type(d))#<class 'dict'>

d={1:"apple"}
print(d)#{1: 'apple'}

d={"a":"apple",1:"one","two":2,3:[1,2,3]}
print(d)#{'a': 'apple', 1: 'one', 'two': 2, 3: [1, 2, 3]}

d={1:"hello",2:"world",3:{'a':"apple",'b':"banan",'c':"carrot"}}
print(d)
#o/p:{1: 'hello', 2: 'world', 3: {'a': 'apple', 'b': 'banan', 'c': 'carrot'}}


#dict cannot have 2 items with the same key
d={'a':"apple",'a':"aeroplane"}
print(d)#keys are not duplicates 
#o/p:{'a': 'aeroplane'}

#keys are case sensitive
d={'A':"apple",'a':"aeroplane"}
print(d)
#o/p:{'A': 'apple', 'a': 'aeroplane'}

d={'a':[1,2,3]}
print(d)#{'a': [1, 2, 3]}

d={[1,2,3]:'a'}
print(d)#unhashable type: 'list'

#items can be added using keys
d={'a':"apple",'b':"ball"}
d['c']="car"
print(d)
#o/p:{'a': 'apple', 'b': 'ball', 'c': 'car'}

#items can be modified using key as index
d={'a':"apple",'b':"ball"}
d['a']="aeroplane"
print(d)
#o/p:{'a': 'aeroplane', 'b': 'ball'}


#clear()
d={1:"one",2:"two"}
print(d.clear())#none

s=d.clear()
print(s)#none

d.clear()
print(d)#{}

#copy()
d={1:"one",2:"two"}
x=d.copy()
print(x)#{1: 'one', 2: 'two'}

print(d)#{1: 'one', 2: 'two'}
print(id(x),id(d))#1877242533568 1877212675392


x[3]="three"
print(x)#{1: 'one', 2: 'two', 3: 'three'}

print(d)#{1: 'one', 2: 'two'}


###get()
d={'a':"apple",'b':"ball",1:"one"}
x=d.get('a')
print(x)#apple

print(d.get(1))#one

z=d.get('s')
print(z)#none



##keys()
d={'a':"apple",'b':"ball",1:"one"}
x=d.keys()
print(x)#dict_keys(['a', 'b', 1])

print(d.keys())#dict_keys(['a', 'b', 1])

##pop()

d={'a':"apple",'b':"ball",1:"one"}
x=d.pop('b')
print(x)#ball

print(d)#{'a': 'apple', 1: 'one'}

y=d.pop(1)
print(y)#one

##popitem()-->ele removed from right to left

d={'a':"apple",'b':"ball",1:"one"}
x=d.popitem()
print(x)#(1, 'one')

print(d.popitem())#('b', 'ball')
print(d)#('b', 'ball')

###setdefault()
d={'a':"apple"}
print(d.setdefault('b',"ball"))#ball
print(d)#{'a': 'apple', 'b': 'ball'}

x=d.setdefault('c',"cat")
print(x)#cat
print(d)#{'a': 'apple', 'b': 'ball', 'c': 'cat'}


###update

d={'a':"apple",'b':"ball",1:"one"}
x={'d':"dog"}
print(x)#{'d': 'dog'}

print(d.update(x))#none

z=d.update(x)
print(z)#none

d.update(x)
print(d)#{'a': 'apple', 'b': 'ball', 1: 'one', 'd': 'dog'}

##values
d={'a':"apple",'b':"ball",1:"one"}
print(d.values())#dict_values(['apple', 'ball', 'one'])

### regular expressions

#re.match() re.search(),re.findall(),re.fullmatch()
import re
input="abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc')
res=re.match(pattern,input)
print(res)#<re.Match object; span=(0, 3), match='abc'>
print(type(pattern))#<class 're.Pattern'>
print(pattern)#re.compile('abc')
res=re.match(pattern,input)
print(res)
#o/p:<re.Match object; span=(0, 3), match='abc'>


import re
input=" abcdefghijklmnopqrstuvwxyz"
pattern=re.compile(r'abc')
res=re.match(pattern,input)
print(res)#None
#print(pattern)


import re
input=" abcdefghijabcklmnopqrsabctuvwxyz"
pattern=re.compile(r'abc')
res=re.match(pattern,input)
print(res)#none
print(pattern)#re.compile('abc')
res=re.search(pattern,input)
print(res)#<re.Match object; span=(1, 4), match='abc'>

import re
input="abcdefghijabcklmnopqrsabctuvwxyz"
pattern=re.compile(r'abc')
text="abc"
res=re.match(pattern,input)
print(res)#<re.Match object; span=(0, 3), match='abc'>
print(pattern)#re.compile('abc')
res=re.search(pattern,input)
print(res)#<re.Match object; span=(0,3), match='abc'>
res=re.findall(pattern,input)
print(res)#['abc', 'abc', 'abc']
res=re.fullmatch(pattern,text)
print(res)#<re.Match object; span=(0, 3), match='abc'>

import re
input=" abcdefghijabcklmnopqrsabctuvwxyz"
pattern=re.compile(r'abc')
text="abcdef"
res=re.match(pattern,input)
print(res)#none
res=re.findall(pattern,input)
print(res)#['abc', 'abc', 'abc']
res=re.fullmatch(pattern,text)
print(res)#none


import re
input=" abcdefghijabcklmnopqrsabctuvwxyz"
text="ABC"
pattern=re.compile(r'abc')
res=re.match(pattern,input)
print(res)#none
res=re.search(pattern,input)
print(res)#<re.Match object; span=(1, 4), match='abc'>
res=re.findall(pattern,input)
print(res)#['abc', 'abc', 'abc']
res=re.fullmatch("abc",text,flags=re.IGNORECASE)
print(res)#<re.Match object; span=(0, 3), match='ABC'>


#re.finditer()
import re
input=" abcdefghijabcklmnopqrsabctuvwxyz"
pattern=re.compile(r'abc')
res=re.finditer(pattern,input)
print(res)

for i in res:
    print(i)


#o/p:<callable_iterator object at 0x0000015FD79206D0>
#<re.Match object; span=(1, 4), match='abc'>
#<re.Match object; span=(11, 14), match='abc'>
#<re.Match object; span=(23, 26), match='abc'>


###re.sub()
import re
input=" abc ndefghij abc klmnopqrs abc tuvwxyz"
pattern=re.compile(r'abc')
res=re.sub(pattern,'xyz',input)
print(res)
#o/p: xyz ndefghij xyz klmnopqrs xyz tuvwxyz


##re.subn()
import re
input=" abc ndefghij abc klmnopqrs abc tuvwxyz"
pattern=re.compile(r'abc')
res=re.subn(pattern,'xyz',input)
print(res)
#o/p:(' xyz ndefghij xyz klmnopqrs xyz tuvwxyz', 3)

pattern=re.compile(r'123')
res=re.subn(pattern,'xyz',input)
print(res)
#o/p:(' abc ndefghij abc klmnopqrs abc tuvwxyz', 0)


###re.split()
import re
input=" abcndefghijabcklmnopqrsabctuvwxyz"
pattern=re.compile(r'abc')
res=re.split(pattern,input)
print("split",res)
#o/p:split [' ', 'ndefghij', 'klmnopqrs', 'tuvwxyz']

###re.escape()
import re
print(re.escape("hii 23445 ./? @ qwe12345#"))

