'''
save A. make database to text files.
'''

from copy import *

database_ion = [[True, 1, 'K+'], [True, 1, 'Na+'], [False, 2, 'SO4--'],[False,1,'Cl-']]

database_comp =  [[{1: 1, 3: 1}, {0.0: 35.65, 10.0: 35.72, 20.0: 35.89, 30.0: 36.09, 40.0: 36.37, 50.0: 36.69, 60.0: 37.04, 70.0: 37.46, 80.0: 37.93, 90.0: 38.47, 100.0: 38.99}], [{1: 2, 2: 1}, {0.0: 4.9, 10.0: 9.1, 20.0: 19.5, 30.0: 40.8, 40.0: 48.8, 60.0: 45.3, 80.0: 43.7, 90.0: 42.7, 100.0: 42.5}], [{4: 1, 2: 1}, {0.0: 23.1, 10.0: 27.5, 20.0: 32.0, 30.0: 37.8, 40.0: 44.6, 60.0: 61.8, 80.0: 83.8, 100.0: 114.0}], [{4: 1, 3: 2}, {0.0: 68.6, 10.0: 70.9, 20.0: 73.0, 30.0: 77.3, 40.0: 87.6, 60.0: 96.5, 80.0: 104.0, 90.0: 108.0, 100.0: 120.0}]]

database_ion_writecopy = deepcopy(database_ion)
database_comp_writecopy1 = deepcopy(database_comp)
database_comp_writecopy2 = []


#save database_ion

##True>>'+', int>>str
for i in range(len(database_ion_writecopy)):
    if database_ion_writecopy[i][0] == True:
        database_ion_writecopy[i][0] ='+'
    elif database_ion_writecopy[i][0] == False:
        database_ion_writecopy[i][0] ='-'
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i][1] = str(database_ion_writecopy[i][1])
print(database_ion_writecopy)
##join
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i]=','.join(database_ion_writecopy[i])
print(database_ion_writecopy)

##write
ion = open("database_ion.txt",'a')
for i in database_ion_writecopy:
    i=i+'\n'
    ion.write(i)
ion.close()



#save database_comp

## seperate keys and values

for i in database_comp_writecopy1:
    temp = []
    for j in i:
        a = list(j.keys())
        b = list(j.values())
        temp = temp + [a] + [b]
    database_comp_writecopy2.append(temp)
a=[]
b=[]
temp = []
print(database_comp_writecopy2)


##all int >> str
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        for k in range(len(database_comp_writecopy2[i][j])):
            database_comp_writecopy2[i][j][k]=str(database_comp_writecopy2[i][j][k])
print(database_comp_writecopy2)

##join step 1. keys and values join
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        database_comp_writecopy2[i][j] = ','.join(database_comp_writecopy2[i][j])
print(database_comp_writecopy2)

##join step 2. comp join
for i in range(len(database_comp_writecopy2)):
    database_comp_writecopy2[i] = '/'.join(database_comp_writecopy2[i])
print(database_comp_writecopy2)

##write
comp = open('database_comp.txt','a')
for i in database_comp_writecopy2:
    i=i+'\n'
    comp.write(i)
comp.close()

#clear all valriables
database_comp_writecopy2 = []
database_comp= []
database_comp_writecopy1= []
database_ion_writecopy= []
database_ion_= []