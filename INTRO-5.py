#FUNCTIONS:-
def myFunction():
    print("hello world")
    x = 1
    y = 3
    print(y + x)

myFunction()

def fullname(first,last): #here 1st and last is not defined..
    print(first + " " + last)

fullname("uddeshya","kumar")#u hav to put both(1st and last) values..or it will show error..

def fulname(initial,middle="jaiswal"):#here middle is defined..
    print(initial + " " + middle)

fulname("raj")#just put 1st (initial) value only...

def addthreenumbers(a=0,b=0,c=0): #default value is 0..
    print(a + b + c)

addthreenumbers(1 ,2 )


def multiplyanddivide(a=0, b=0):
    return(a*b, a/b)

(c1,c2) = multiplyanddivide(15,3)
print(c1)
print(c2)

#lambda Expressions:-

f = lambda x,y: 2*x + x ** 2 + 5*y
print(f(2,4))



#DATETIME
import datetime as dt

date = dt.datetime.now()
print(date.year)
print(date.hour)
print(date.minute)

myOwndate = dt.datetime(1996,10,3)
print(myOwndate)

if myOwndate > date:
    print("my owndate is ahead")
else:
    print("my owndate is behind")

#JSon




























