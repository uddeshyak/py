#Boolean operator(true/false)
print(1 <=2)
print(3 <=2)

x = 14
y = -15
print(x == y) #tetsing if they are  equal
print(x != y) #tetsing if they are not equal
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y) and (x != y) #if your require both statement to be true

#4 type of arrays
# 1)Lists: is a collection, which is ordered and changeable
fruits = ["Apples", "cherries", "Bananas", "Pineapples"] #apple is at index=0,cherries at 1 and so on..
print(fruits)
print(fruits[0])

fruits[1] = "avocado" #it will change cherries to avocado
fruits[2] = "grapes"
fruits.insert(4,"guava")

print(fruits)
fruits.remove("Apples")
print(fruits)
print(len(fruits))

fruits.sort() #it will sort alphabetically
print(fruits)

       #LOOP
for W in fruits:
    print(W)  #it will print name of fruits
for W in fruits:
    print(W[0]) #it will print initials of fruits

numbers = [10,2,8,-5,16,0]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)


# 2)Tuples:is a collection which is ordered and unchangeable..it is defined by using parenthesis()..
aTuple = (3,5,10)
#we cannot change/modify/replace(.i.e.unchangeable) anything  in parenthesis()..
#visit wwww.programiz.com to read about it

# 3)Sets:is a collection which is UNordered and UNchangeable,,it is defined by using curly bracket{}
#UNchangeable means same as above...UNordered means below nos. are not sitting at thier place like -4 at 0....

myset ={-4,10,3,11,-5}
print(myset)
myset.add(100)
print(myset) #it add 100 randomly at any index/position


# 4)Dictionaries: [key/value] pairs  (UNordered and changeable and indexed)
#use curly bracket{} for dictionaries
#While indexing is used with other data types to access values, a dictionary uses keys.
#Keys can be used either inside square brackets [] or with the get() method.
myDictionary = {"key1": 10, "key2": 20, "key3": 15, "key4": 12}
print(myDictionary)
print(myDictionary["key1"])
print(myDictionary.get("key2"))
for x in myDictionary:
    print(x) #it only print key..not value..
for x in myDictionary:
    print(myDictionary[x]) #it will print values..
for x in myDictionary:
    print("x: " + x + ", value: " + str(myDictionary[x]))\

myDictionary["key1"] = 90 #changing values
print(myDictionary)
print(len(myDictionary))
del myDictionary["key1"] #deleting keys
print(myDictionary)

print(myDictionary.keys()) #it will show all keys u have..

myDictionary.clear()
print(myDictionary) #it will clear all content..



















