#Strings
'''
indexing : 0-(len-1)
length : the actual no of strings
negative index is length  -length 

'''

#String Slicing 
name = "Tauseef"
print(name)

print(len(name))
print(name[0])
print(name[-6])

sl = name
print(sl[0:3])
print(sl[1:6:2]) # start,end,skip skip value should always be > 1 and less than len of string

#String Functions
print(len(sl)) 
print(sl.endswith("ee"))
print(sl.endswith("ef"))
print(sl.startswith("ta"))
print(sl.startswith("Ta"))
print(sl.count('e')) #Occurence 
print(sl.capitalize())
print(sl.find("eef"))
print(sl.replace("eef","fee"))



#PG1 User Entered name followed by GAF using input() function

name = input("Enter Your Name: ")
print("Good After Noon,",name)


#PG2 
name = input("Enter Your Name: ")
date = input("Enter date: ")
letter = ("Dear " + name +  " You are Born on: " + date)
print(letter)

