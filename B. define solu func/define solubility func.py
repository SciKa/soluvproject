database_comp =  [[{1: 1, 3: 1}, {0.0: 35.65, 10.0: 35.72, 20.0: 35.89, 30.0: 36.09, 40.0: 36.37, 50.0: 36.69, 60.0: 37.04, 70.0: 37.46, 80.0: 37.93, 90.0: 38.47, 100.0: 38.99}], [{1: 2, 2: 1}, {0.0: 4.9, 10.0: 9.1, 20.0: 19.5, 30.0: 40.8, 40.0: 48.8, 60.0: 45.3, 80.0: 43.7, 90.0: 42.7, 100.0: 42.5}], [{4: 1, 2: 1}, {0.0: 23.1, 10.0: 27.5, 20.0: 32.0, 30.0: 37.8, 40.0: 44.6, 60.0: 61.8, 80.0: 83.8, 100.0: 114.0}], [{4: 1, 3: 2}, {0.0: 68.6, 10.0: 70.9, 20.0: 73.0, 30.0: 77.3, 40.0: 87.6, 60.0: 96.5, 80.0: 104.0, 90.0: 108.0, 100.0: 120.0}]]
#저것은 원래는 다를 수 잇따.

import numpy as np
import scipy.interpolate as ip
from scipy.interpolate import splrep, splev
import matplotlib.pyplot as plt

def solubility(compcode, temp): #compcode는 화합물 데이터베이스의 인덱스를 말한다. 그러니까, NaCl이 3번째에 저장되있음 3. 정수형.
    dict_solubability = database_comp[compcode][1]
    list_temp = list(dict_solubability.keys())
    list_solu = list(dict_solubability.values()) # 이 둘은 모두 float 로만 이뤄진 리스트이다.
    x = np.array(list_temp)
    y = np.array(list_solu)
    spl = splrep(x, y)
    x1 = np.linspace(0, 100, 1000)
    y1 = splev(x1, spl)
    return splev(temp, spl)

def solugraph(compcode):
    dict_solubability = database_comp[compcode][1]
    list_temp = list(dict_solubability.keys())
    list_solu = list(dict_solubability.values())  # 이 둘은 모두 float 로만 이뤄진 리스트이다.
    x = np.array(list_temp)
    y = np.array(list_solu)
    spl = splrep(x, y)
    x1 = np.linspace(0, 100, 1000)
    y1 = splev(x1, spl)

    plt.plot(x1, y1, label="soludot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title('solubility')
    plt.legend()
    plt.show()


B_ask_comp = int(input('put comp number.'))
#B_ask_tenmp =  float(input('put temp'))
solugraph(B_ask_comp) #이게 solubility 함수보다 뒤에 오면 그래프 창이 닫힐 때 까지 다른 코드가 중단됨.
#print (solubility(B_ask_comp,B_ask_tenmp))


    