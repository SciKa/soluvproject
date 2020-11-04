database_ion = [[True, 1, 'K+'], [True, 1, 'Na+'], [False, 2, 'SO4--'],[False,1,'Cl-']]

print('ion charge', '|','ion name')
for i in range(len(database_ion)):
    
    if database_ion[i][0] == True:
        print(' '*(11 - database_ion[i][1]),end = '')
        print('+'*database_ion[i][1],end = '')
    elif database_ion[i][0] == False:
        
        print(' '*(11 - database_ion[i][1]),end = '')
        print('-'*database_ion[i][1],end = '')

    print('|',database_ion[i][2])
