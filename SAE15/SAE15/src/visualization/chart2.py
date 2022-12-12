from operator import itruediv
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import os, glob
import analysr
path = "../../data/cleaned/"
all_files = glob.glob(os.path.join(path, "*.csv"))

print(all_files)
df= pd.read_csv(all_files[0])
main = analysr.difflike(df)
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
p6 = []
p0 = []
for item in main:
    if 0 < item < 10:
        p1.append(item)
    elif 20 < item < 50:
        p2.append(item)
    elif 50 < item < 75:
        p3.append(item)
    elif 75 < item < 100:
        p4.append(item)
    elif 100 < item < 200:
        p5.append(item)
    elif 10 < item < 20:
        p0.append(item)
    else:
        p6.append(item)


city = ['0->10','10->20', '20->50', '50->75', '75->100', '100->200','200 ->']
pos = np.arange(len(city))
Happiness_Index=[len(p0),len(p1),len(p2),len(p3),len(p4),len(p5),len(p6)]
for item in Happiness_Index:
    print(item)

plt.bar(pos,Happiness_Index,color='orange',edgecolor='black')
plt.xticks(pos, city)
plt.ylabel('NB Vidéos', fontsize=16)
plt.title('Ratio Likes / Dislikes',fontsize=20)
plt.show()