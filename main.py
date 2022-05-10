import pandas as pd
import math
n=15
print("H0: u is from the large population")
print("H1: u is not from the large population\n\n")
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
t = (m1 - m2) / sed
print("Calculated t value =",t)

if t < 1.96 and t > -1.96:
        print("\nretain H0, this sample is from the large population")
else:
    print("\nreject H0,this sample is not from the large population")