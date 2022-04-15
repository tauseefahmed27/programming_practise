#Lists......
#Collection of values of any datatype and mutable i.e changeable.
#Methods/Operataion on Lists: Sort, reverse, append, insert, pop, remove


a = ['Syed','Tauseef',27,'MJCET',8.2]
print("Students details are as follows:")
details =['Firstname:', 'MiddleName:', 'Age:', 'College:', 'CGPA:']
print(details)
print(a)
details.insert(2,"LastName:")
a.insert(2,"Ahmed")
print(details)
print(a)

a.pop()
print(a)


#Tuples.....
#only a single typr of datatype
#Immutable datatype, i.e cannot be changed!
#Methods :  count, index! 


aTuple = (3,2,7)
print(aTuple)


#PractiseSet

#Q1: seven fruits in a list entered by user

#using for loop but incorrect way 
fruitList = []
print("Welcome to fruit Shop!, Please enter you favourite 7 fruits names to make a fruit salad")
for i in range(7):
    a = input("Enter Fruits names ")
    fruitList.append(a)
print(fruitList)

#Simple
f1 = input("Enter Fruity Fruit 1: ")
f2 = input("Enter Fruity Fruit 2: ")
f3 = input("Enter Fruity Fruit 3: ")
f4 = input("Enter Fruity Fruit 4: ")
f5 = input("Enter Fruity Fruit 5: ")
fruityList = [f1,f2,f3,f4,f5]
print(fruityList)

#Q2: Marks of 5y student and sort them in order


s1 = input("Marks of Student 1 :")
s2 = input("Marks of Student 2 :")
s3 = input("Marks of Student 3 :")
s4 = input("Marks of Student 4 :")
s5 = input("Marks of Student 5 :")
studentMarks = [s1,s2,s3,s4,s5]
print(studentMarks)
studentMarks.sort()
print(studentMarks)


#Q3: Sum a list with 4 numbers

myList = [1, 2, 4, 5]
myList.append(int(input("Enter Values")))
myList.append(int(input("Enter Values")))
myList.append(int(input("Enter Values")))
myList.append(int(input("Enter Values")))

sum = 0
sum += myList[0]
sum += myList[1]
sum += myList[2]
sum += myList[3]
print("Value of Sum is ", sum)

