import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
import os, glob
import analysr
path = "../../data/cleaned/"
all_files = glob.glob(os.path.join(path, "*.csv"))

print(all_files)
df= pd.read_csv(all_files[0])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
temp = analysr.nbmorelike(df)
langs = ['Plus de Like que de Dislikes', 'Plus de dislike que de likes']
prc = [temp[0],temp[1]]
myexplode = [0, 0.2]
mycolors = ["green", "red"]

ax.pie(prc, labels = langs,autopct='%1.2f%%',explode = myexplode,pctdistance=1.3, labeldistance=1.5,colors = mycolors)

plt.legend() 
plt.show()