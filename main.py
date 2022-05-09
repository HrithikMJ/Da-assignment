import pandas as pd
import math
n=24
df1=pd.read_csv("Kaggle_Upload.csv")
m1=df1["Total Confirmed cases "].mean()
m2=df1["Death"].mean()
sd1=df1["Total Confirmed cases "].std()
sd2=df1["Death"].std()
se1=sd1/math.sqrt(n)
se2=sd2/math.sqrt(n)
ss1=se1**2
ss2=se2**2
sed = math.sqrt(ss1*ss2)
t_stat = (m1 - m2) / sed
print(t_stat)