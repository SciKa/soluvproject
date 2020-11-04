'''
read textfiles to real A. make database.
'''

from copy import *

database_comp_writecopy2 = []
database_comp= []
database_comp_writecopy1= []
database_ion_writecopy= []
database_ion = []



#read database_ion

##read
ion = open("database_ion.txt",'r')
database_ion_writecopy = ion.readlines()
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i] = database_ion_writecopy[i].strip('\n')

ion.close()
print(database_ion_writecopy)

##split
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i]=database_ion_writecopy[i].split(',')
print(database_ion_writecopy)

##True<<'+', int<<str
for i in range(len(database_ion_writecopy)):
    if database_ion_writecopy[i][0] == '+':
        database_ion_writecopy[i][0] =True
    elif database_ion_writecopy[i][0] == '-':
        database_ion_writecopy[i][0] =False
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i][1] = int(database_ion_writecopy[i][1])
print(database_ion_writecopy)

##clear database_ion_writecopy and save it to database_ion
database_ion = deepcopy(database_ion_writecopy)
database_ion_writecopy = []

print(database_ion)


#read database_comp

##read
comp = open("database_comp.txt",'r')
database_comp_writecopy2 = comp.readlines()
for i in range(len(database_comp_writecopy2)):
    database_comp_writecopy2[i] = database_comp_writecopy2[i].strip('\n')
comp.close()
print(database_comp_writecopy2)



##join step 2. comp join
for i in range(len(database_comp_writecopy2)):
    database_comp_writecopy2[i]=database_comp_writecopy2[i].split('/')
print(database_comp_writecopy2)

##join step 1. keys and values join
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        database_comp_writecopy2[i][j] = database_comp_writecopy2[i][j].split(',')
print(database_comp_writecopy2)

##all int <<< str
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        if j<= 1:
            for k in range(len(database_comp_writecopy2[i][j])):
                database_comp_writecopy2[i][j][k] = int(database_comp_writecopy2[i][j][k])
        elif j>1:
            for k in range(len(database_comp_writecopy2[i][j])):
                database_comp_writecopy2[i][j][k] = float(database_comp_writecopy2[i][j][k])

print(database_comp_writecopy2)

## seperate keys and values
temp = []
for i in range(len(database_comp_writecopy2)):
    temp = []
    key1 = []
    key2 = []
    value1 = []
    value2 = []

    key1 = database_comp_writecopy2[i][0]
    value1 = database_comp_writecopy2[i][1]
    key2 = database_comp_writecopy2[i][2]
    value2 = database_comp_writecopy2[i][3]

    a = dict(list(zip(key1, value1)))
    b = dict(list(zip(key2, value2)))
    temp = temp + [a] + [b]

    database_comp_writecopy1.append(temp)
print(database_comp)
##clear database_ion_writecopy and save it to database_ion
database_comp = deepcopy(database_comp_writecopy1)
database_comp_writecopy1 = []
database_comp_writecopy2 = []

temp = []
key1 = []
key2 = []
value1 = []
value2 = []
a=[]
b=[]

print(database_comp)