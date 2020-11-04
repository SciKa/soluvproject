'''
forming compound A. make database before record it on txt. file
compound data has four properties: code(indexed), data, ion info.
and each has very difficult sth.
'''
# ask properties.
database_ion_name = ['K+','Na+','SO4--','Cl-'] # it would be brought by ion data. plz look /makeiondata
database_comp = []
database_comp_name = []



for i in range(2):

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

    MW = input('분자량? :')
    MW = float(MW)
    while True:
        temperature = input('온도? :')
        if temperature == 'done':
            break
        solubility = input('용해도? :')
        if solubility == 'done':
            break
        temperature = float(temperature)
        solubility = float(solubility)
        molar_solub = (solubility / MW) * 10
        dict_solvdata[temperature] = solubility


    b = [dict_ioninfo, dict_solvdata]
    database_comp = database_comp + [b]

print(database_comp)




# example of name part only list.

b = [{1: 2, 2: 1}, {0.0: 5.0, 25.0: 20.0, 33.0: 50.0, 50.0: 47.0, 75.0: 43.0, 100.0: 42.0}]
database_comp = [b]

for i in range(len(database_comp)):
    database_comp_name = database_comp_name + [database_comp[i][0]]

print(database_comp)
print(database_comp_name)
