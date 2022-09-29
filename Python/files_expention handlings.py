### EXCEPTION HANDLING

EX1:
print(10/0)
#o/p:ZeroDivisionError


EX2:
a=int(input("enter a number:"))
print(a)
o/p:ValueError

EX3:
a=10
print(A)
o/p:NameError

EX4:
print(10+"hello")
o/p:TypeError


Ex:file1.py 

f = open("sample.txt",'w')
print("file name is :",f.name)
print("file mode is :",f.mode)
print("is file readable ? :",f.readable())
print("is file writable ? :",f.writable())
print("is file closed ? :",f.closed)
f.close()
print("is file closed ? :",f.closed)

o/p:file name is : sample.txt
file mode is : w
is file readable ? : False
is file writable ? : True
is file closed ? : False
is file closed ? : True

### WRITE

Ex:file2.py

f = open("abc.txt",'w')
f.write("Hello\n")
f.write("how are you\n")
f.write("welcome\n")
print("data is written in the file")
f.close()

o/p:
Hello
how are you
welcome

###APPEND

EX:file3.py

f = open("abc.txt",'a')
f.write("Hello\n")
f.write("how are you\n")
f.write("welcome\n")
print("data is written in the file")
f.close()

o/p:

Hello
how are you
welcome
Hello
how are you
welcome

### WRITELINES

f=open("xyz.txt",'w')
l=["sai\n","mohan\n","sree\n","rama\n"]
f.writelines(l)
print("list data written to the file successfully")
f.close()

o/p:sai
mohan
sree
rama

### EXCLUSIVE 

f=open("abc.txt",'x')
f.write("Hello\n")
print("Data written in the file")
f.close()

o/p

f=open("abc.txt",'x')
FileExistsError: [Errno 17] File exists: 'abc.txt'


### READ FILE

EX:1

try:
    f=open("123.txt",'r')
    data=f.read()
    print(data)
    f.close()
except FileNotFoundError as msg:
    print(msg)
o/p:[Errno 2] No such file or directory: '123.txt'

          (or)
another  method:

    f=open("123.txt",'r')
    data=f.read()
    print(data)
    f.close()
o/p:    f=open("123.txt",'r')
FileNotFoundError: [Errno 2] No such file or directory: '123.txt'
because the file doesnot exist .If file is exist it will be read

EX:2

f=open("abc.txt",'r')
data=f.read()
print(data)
f.close()

o/p:Hello
how are you
welcome
Hello
how are you
welcome

EX:3--->read(n)

f=open("abc.txt",'r')
data=f.read(10)
print(data)
f.close()

o/p:
Hello
how

EX:4--->readline()

f=open("abc.txt",'r')
data=f.readlines()
print(data)
f.close()
o/p:Hello



EX:5---> readlines()

f=open("abc.txt",'r')
data=f.readlines()
print(data)
f.close()

o/p:['\n', 'Hello\n', 'how are you\n', 'welcome\n', 'Hello\n', 'how are you\n', 'welcome']


EX:6

f=open("abc.txt",'r')
data=f.read(5)
print(data)
str=f.read(10)
print(str)
position=f.tell()
print("position of cursor is :",position)
f.close()
