import analysr
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np
df= pd.read_csv('merged.csv')

a=analysr.checklong(df,'video_id',11)
b=analysr.checklong(df,'trending_date',8)
c=analysr.checkcol(df,'title',str)
d=analysr.checkcol(df,'channel_title',str)
e=analysr.checkcol(df,'category_id',int)
f=analysr.checkcdate(df,'publish_time',)
g=analysr.checkcol(df,'tags',str)
h=analysr.checkcol(df,'views',int)
i=analysr.checkcol(df,'likes',int) 
j=analysr.checkcol(df,'comment_count',int)
k=analysr.checkcarac(df,'thumbnail_link')
l=analysr.checkcol(df,'comments_disabled',bool)
m=analysr.checkcol(df,'ratings_disabled',bool)
n=analysr.checkcol(df,'video_error_or_removed',bool)
o=analysr.checkcol(df,'description',str)
p=analysr.checkcol(df,'dislikes',int)
    #print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)
cell= int(df.shape[0]*df.shape[1])
er=int(len(a)+len(b)+len(c)+len(d)+len(e)+len(f)+len(g)+len(h)+len(i)+len(j)+len(k)+len(l)+len(m)+len(n)+len(o)+len(p))
print(er)
print(analysr.nbempty(df))
pourc1= (er/cell)*100
pourc2= ((er - analysr.nbempty(df))/cell)*100
pourc3= (analysr.nbempty(df)/cell)*100

print(pourc1,pourc2,pourc3)
'video_id', 'trending_date', 'title', 'channel_title', 'category_id', 'publish_time', 'tags', 'views', 'likes', 'dislikes', 'comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description'

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['Donnée Correcte', 'Donnée Vide', 'Donnée Eronner']
prc = [(100-pourc1),pourc2*5,pourc3]
myexplode = [0, 1,1]
mycolors = ["blue", "red", "green"]

ax.pie(prc, labels = langs,autopct='%1.2f%%',explode = myexplode,pctdistance=1.3, labeldistance=1.5,colors = mycolors)

plt.legend() 
plt.show()
#plt.savefig('foo.png')