# 데이터분석 라이브러리 판다스 x 맷플롭립
# https://ordo.tistory.com/34?category=732886
import pandas as pd # pip install pandas
from pandas import DataFrame as df

df1 = df(data={'Num':['1', '2', '3'], 'Name':['Kim', 'Park', 'Choi'], 'Color':['red', 'blue', 'green']})
print(df1)
df2 = df