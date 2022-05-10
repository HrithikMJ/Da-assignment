import pandas as pd
import math
n=15
u=134.25714285714287
sd=368.40030520338826
print("\n\nH0: u has similar deaths\n")
print("H1: u doesnt have similar death\n\n")
df1=pd.read_csv("Kaggle_Upload.csv")
m=df1["Death"].mean()
sd=df1["Death"].std()
se2=sd/math.sqrt(n)
z= (m - u) / se2
print("Calculated t value =",z)

if z < 1.96 and z > -1.96:
        print("\nretain H0, this sample is has similair death")
else:
    print("\nreject H0,this sample doesnot have similair death")