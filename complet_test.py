#0. 함수 정의

def solubility(compcode, temp): #compcode는 화합물 데이터베이스의 인덱스를 말한다. 그러니까, NaCl이 3번째에 저장되있음 3. 정수형.
    dict_solubability = database_comp[compcode][1]
    list_temp = list(dict_solubability.keys())
    list_solu = list(dict_solubability.values()) # 이 둘은 모두 float 로만 이뤄진 리스트이다.
    lowvalue = 0
    highvalue = 0
# 온도가 어디에 있는지 구하기
    for i in range(len(list_temp)):

        if list_temp[i]>= temp:
            lowvalue = list_temp[i-1]
            highvalue = list_temp[i]
            break


    return ((dict_solubability[highvalue]-dict_solubability[lowvalue])/(highvalue-lowvalue))*(temp - lowvalue) +dict_solubability[lowvalue]


#1. 읽어오기로 시작함
from copy import *

database_comp_writecopy2 = []
database_comp= []
database_comp_writecopy1= []
database_ion_writecopy= []
database_ion = []
database_ion_name = []

#read database_ion

##read
ion = open("database_ion.txt",'r')
database_ion_writecopy = ion.readlines()
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i] = database_ion_writecopy[i].strip('\n')

ion.close()


##split
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i]=database_ion_writecopy[i].split(',')


##True<<'+', int<<str
for i in range(len(database_ion_writecopy)):
    if database_ion_writecopy[i][0] == '+':
        database_ion_writecopy[i][0] =True
    elif database_ion_writecopy[i][0] == '-':
        database_ion_writecopy[i][0] =False
for i in range(len(database_ion_writecopy)):
    database_ion_writecopy[i][1] = int(database_ion_writecopy[i][1])


##clear database_ion_writecopy and save it to database_ion
database_ion = deepcopy(database_ion_writecopy)
database_ion_writecopy = []




#read database_comp

##read
comp = open("database_comp.txt",'r')
database_comp_writecopy2 = comp.readlines()
for i in range(len(database_comp_writecopy2)):
    database_comp_writecopy2[i] = database_comp_writecopy2[i].strip('\n')
comp.close()




##join step 2. comp join
for i in range(len(database_comp_writecopy2)):
    database_comp_writecopy2[i]=database_comp_writecopy2[i].split('/')


##join step 1. keys and values join
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        database_comp_writecopy2[i][j] = database_comp_writecopy2[i][j].split(',')


##all int <<< str
for i in range(len(database_comp_writecopy2)):
    for j in range(len(database_comp_writecopy2[i])):
        if j<= 1:
            for k in range(len(database_comp_writecopy2[i][j])):
                database_comp_writecopy2[i][j][k] = int(database_comp_writecopy2[i][j][k])
        elif j>1:
            for k in range(len(database_comp_writecopy2[i][j])):
                database_comp_writecopy2[i][j][k] = float(database_comp_writecopy2[i][j][k])



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


####make A. make database ion name
for i in range(len(database_ion)):
    database_ion_name = database_ion_name + [database_ion[i][2]]
##make namt_list
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

#2. 메뉴w
while True:
    print('환영합니다.')
    print('메뉴 중 원하는 기능을 선택하세요.')
    print('0...이온 데이터 추가\n1...이온결합화합물 데이터 추가\n2...용해도 추정\n3... 데이터 보기\nstop...프로그램 종료')
    select = input(':::')

    if select == '0':
        # ask properties
        code = 0
        charge = 0
        sign = True
        name = ''

        A_select = int(input('데이터베이스에 추가할 이온의 수를 입력하세요.'))

        for i in range(A_select):  # 이 부분을 입력받으면 되는거임.

            code = 0
            charge = 0
            sign = True
            name = ''

            name = input('이온의 이름을 //중요// 다음과 같이 넣어주세요. 예시) NH4+, SO4--\n이온의 이름?:')

            while True:
                sign_temp = input('이온의 전하를 정해주세요.\n0...이온이 앙전하 1...이온이 음전하 :')
                if sign_temp == '0':
                    sign = True
                    break
                elif sign_temp == '1':
                    sign = False
                    break
                else:
                    print('0 또는 1만 입력가능')

            charge = int(input('이온의 전하량을 넣어주세요. :'))

            a = [sign, charge, name]
            database_ion = database_ion + [a]
            # making A. make database part. can change.
        print('저장중...')
        database_ion_writecopy = deepcopy(database_ion)
        # save database_ion

        ##True>>'+', int>>str
        for i in range(len(database_ion_writecopy)):
            if database_ion_writecopy[i][0] == True:
                database_ion_writecopy[i][0] = '+'
            elif database_ion_writecopy[i][0] == False:
                database_ion_writecopy[i][0] = '-'
        for i in range(len(database_ion_writecopy)):
            database_ion_writecopy[i][1] = str(database_ion_writecopy[i][1])
        print(database_ion_writecopy)
        ##join
        for i in range(len(database_ion_writecopy)):
            database_ion_writecopy[i] = ','.join(database_ion_writecopy[i])
        print(database_ion_writecopy)

        ##write
        ion = open("database_ion.txt", 'w')
        for i in database_ion_writecopy:
            i = i + '\n'
            ion.write(i)
        ion.close()
        database_ion_writecopy = []
        print('저장되었습니다.')

    elif select == '1':
        B_select = int(input('데이터베이스에 추가할 이온결합화합물의 수를 입력하세요.'))

        for i in range(B_select):  # 이 부분을 입력받으면 되는거임.

            dict_ioninfo = {}
            dict_solvdata = {}

            ## ask ion info.
            print('이온결합 물질의 화학식을 입력합니다. 다음 규칙에 맞게 입력해주세요.')
            print('1. 추가하고 싶은 이온결합물질의 화학식을 떠올리세요. 예시) 황산암모늄 (NH4)2SO4')
            print('2. 물질의 구성 이온 중 하나를 //중요//아래첨자(계수)를 뺀 뒤 이온의 전하량과 같이 적어주세요. \n 예시1)NH4+, 예시2)SO4--')
            print('3. 적은 물질의 아래첨자(계수)를 적어주세요. 예시) 2')
            print('4. 화합물을 이루는 모든 이온에 대해 이하 과정을 반복했으면, done 를 입력해주세요')
            while True:

                name = input('이온의 이름은? :')
                if name == 'done':
                    break
                num = input('이온의 계수는? :')
                if num == 'done':
                    break
                code_name = database_ion_name.index(name)
                dict_ioninfo[code_name] = int(num)

            ## ask data.
            print('이온결합 물질의 용해도 실험값을 입력합니다. 다음 규칙에 맞게 입력해주세요.')
            print('1. 추가하고 싶은 용해도 데이터를 떠올리세요. 예시) 153, 35도에서.')
            print('2. 이 프로그램은 몰랄 용해도를 사용합니다. 프로그램은 자동으로 질량 용해도를 몰랄 용해도로 바꾸어 줍니다.\n 분자량이 필요합니다. 분자량을 입력하세요.')
            print('3. 용해도를 측정한 온도를 적어주세요.')
            print('4. 용해도를 적어주세요. 마찬가지로 모든 과정을 반복했으면, done 을 입력하세요.')

            #MW = input('분자량? :')
            #MW = float(MW)
            while True:
                temperature = input('온도? :')
                if temperature == 'done':
                    break
                solubility = input('용해도? :')
                if solubility == 'done':
                    break
                temperature = float(temperature)
                solubility = float(solubility)
                #molar_solub = (solubility / MW) * 10
                dict_solvdata[temperature] = solubility

            b = [dict_ioninfo, dict_solvdata]
            database_comp = database_comp + [b]

        print(database_comp)
        print('저장중...')
        # save database_comp

        ## seperate keys and values
        database_comp_writecopy1 = deepcopy(database_comp)
        for i in database_comp_writecopy1:
            temp = []
            for j in i:
                a = list(j.keys())
                b = list(j.values())
                temp = temp + [a] + [b]
            database_comp_writecopy2.append(temp)
        a = []
        b = []
        temp = []
        print(database_comp_writecopy2)

        ##all int >> str
        for i in range(len(database_comp_writecopy2)):
            for j in range(len(database_comp_writecopy2[i])):
                for k in range(len(database_comp_writecopy2[i][j])):
                    database_comp_writecopy2[i][j][k] = str(database_comp_writecopy2[i][j][k])
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
        comp = open('database_comp.txt', 'w')
        for i in database_comp_writecopy2:
            i = i + '\n'
            comp.write(i)
        comp.close()
        database_comp_writecopy2 = []
        database_comp_writecopy1 = []
        print('저장되었습니다.')
    elif select == '2':

        a = str(input('화합물 데이터베이스에서 찾을 수 있는 화합물을입력하세요. 정수형입니다.'))
        b = float(input('원하는 온도를 0도~100도 범위 내에서 입력하세요.'))
        
        c = solubility(namt_list.index(a),b)
        print(b, '도 에서의 ', a, '의 용해도는,', c, '입니다.')
    elif select == 'stop':
        print('종료합니다. 모든 내용이 저장되었습니다.')
        break
    elif select == '3':
        for i in database_ion:
            print(i)
        for i in database_comp:
            print(i)
        print('위의 이온 리스트를 통해 화합물의 종류를 읽을 수 있습니다.')
        print('이온 데이터: [True=양이온False=음이온,전하의 크기, 이온 이름]')
        print('화합물 데이터: [{이온 번호:물질에 포함된 해당 이온 수},{온도:용해도}]')



