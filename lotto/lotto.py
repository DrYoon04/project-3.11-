import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
file = 'lottolist1.xlsx'
#파일 불러오기(macos.ver)
sn = 'lottolist'#찾는 시트명 설정
sp = 'N:S'#읽을 위치 설정
data = pd.read_excel(file, sheet_name = sn,usecols = sp,skiprows=2)
data.round(0).astype(int)#소수점 제거
data.reset_index(drop=True)#색인 초기화

data1cnt = data[1].value_counts()#각 열 숫자 세기 
data2cnt = data[2].value_counts()
data3cnt = data[3].value_counts()
data4cnt = data[4].value_counts()
data5cnt = data[5].value_counts()
data6cnt = data[6].value_counts()

df = pd.DataFrame(data=[data1cnt,data2cnt,data3cnt,data4cnt,data5cnt,data6cnt])#뭐지? 이게 이렇게 쉬운거였다고? 나죽어!!
df.fillna(0)
sumdf = df.sum()
sumdf.plot(kind='bar')
plt.show()
print(sumdf.nlargest(6))
