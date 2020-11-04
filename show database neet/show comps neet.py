database_comp = [[{1: 2, 2: 1}, {0.0: 9.0, 10.0: 31.0, 20.0: 34.0, 30.0: 37.0, 40.0: 40.0, 50.0: 13.5, 60.0: 45.5, 70.0: 48.3, 80.0: 51.1, 90.0: 54.0, 100.0: 50.0}],[{0: 1, 3: 1}, {10.0: 30.0, 30.0: 35.0, 50.0: 42.0, 70.0: 48.0, 90.0: 55.0}], [{0: 2, 2: 1}, {25.0: 25.0, 50.0: 30.0, 75.0: 40.0, 100.0: 49.0}],[{1: 1, 3: 1}, {0.0: 35.7, 40.0: 36.3, 80.0: 38.0, 100.0: 39.0}]]
database_ion = [[True, 1, 'K+'], [True, 1, 'Na+'], [False, 2, 'SO4--'],[False,1,'Cl-']]
databasenamt = ''
namt_temp = ''
namt_key1 = []
namt_valu1 = []
namt_key2 = []
namt_valu2 = []
namt_list = []
for i in range(len(database_comp)):
    namt_key1 = []
    namt_valu1 = []
    namt_key2 = []
    namt_valu2 = []
    
    namt_key1 = list(database_comp[i][0].keys())
    namt_valu1 = list(database_comp[i][0].values())
    namt_key2 = list(database_comp[i][1].keys())
    namt_valu2 = list(database_comp[i][1].values())

    for i in range(2):
        
        namt_temp2 = database_ion[namt_key1[i]][2].replace('+','',10)
        namt_temp3 = namt_temp2.replace('-','',10)
        

        numtt = namt_valu1[i]
        numttt = str(numtt)
        databasenamt = databasenamt +'(' + namt_temp3 + ')'   + numttt


    namt_list = namt_list + [databasenamt]
    databasenamt = ''

    




#find namt_list>>code::index!!!!
