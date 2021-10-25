x = 5 #integer
print(float(x))
name = "raj"  #string

y = 5.23 #float
print(type(name))

z = 1 + 2j; #complex
print(type(z))

firtname = "doctor raj"
lastname = "kumar"

fullname = firtname + " " + lastname
print(fullname)
#if you want to concatenate integer to text, you hav to use "str()",otherwise it wil show error.
fullname = firtname + " " + lastname + str(x)
print(fullname)
print(firtname.upper())
print(firtname.replace("j","zZ"))
print(firtname.split(" "))
print(firtname.split("o"))

#print("what is your full name")
#name = input()
#print("Greetings, " + name)
#{remove HASHTAG to understand}


#OPERATORS
print(x+y)
print(x-y)
print(x*y)
print(x/y)

v = 24
w = 20
o = 10
p = 3
print (float(w)/float(x))
print(v % x )
print(w ** x ) #exponentiation
print(o // p ) #floor division....closest to 3.333333 is 3.

d =12
d = d + 1
d += 2
print(d)#we can also apply *,- / modular..etc












