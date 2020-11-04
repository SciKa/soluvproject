'''
forming ion A. make database before record it on txt. file
ion data has four properties: code(indexed), + or -, charge, name.
'''

#ask properties
database_ion_name = []
database_ion = []
code = 0
charge = 0
sign = True
name = ''




for i in range(3): # 이 부분을 입력받으면 되는거임.

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
print(database_ion)






'''
#example of making name part only list.

a = [True,2,'Ca']
database_ion = [a]

for i in range(len(database_ion)):
    database_ion_name = database_ion_name + [database_ion[i][2]]

print(database_ion)
print(database_ion_name)
'''