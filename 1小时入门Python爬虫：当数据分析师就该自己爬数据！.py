
# coding: utf-8

# # 获取去哪儿网数据
# 批量获取页面
# In[89]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url="https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-2"
urllist = []
ui="https://travel.qunar.com/p-cs299878-shanghai-jingdian-1-"
for i in [1,2,3,4]:
    u=ui+str(i)
    urllist.append(u)
    

# 访问页面
# In[8]:


u1=urllist[0]
r=requests.get(u1)

soup=BeautifulSoup(r.text,"lxml")
soup.title


# In[59]:


ul=soup.find("ul",class_="list_item clrfix")      #根据网页的结构分析，景点名称都在ul下
li=ul.find_all("li")                                           #ul下都是li标签，对ul进行标签寻找，找出每一个景点
li[0].text

#用字典去存储数据
# In[56]:


dic={ }
li1=li[0]

dic["景点名称"]=li1.find("span",class_="cn_tit").text.split("：")[0]
dic["攻略数目"]=li1.find("div",class_="strategy_sum").text
dic["评论数"]=li1.find("div",class_="comment_sum").text
dic["排名"]=li1.find("span",class_="ranking_sum").text
dic["星级"]=li1.find("span",class_="total_star").find("span")["style"].split(":")[1]
dic["描述"]=li1.find('div',class_="desbox").text

#批量的去采集上述信息
# In[60]:


datai=[]
for i in li:
    
    dic={ }
    
    dic["景点名称"]=i.find("span",class_="cn_tit").text.split("：")[0]
    dic["攻略数目"]=i.find("div",class_="strategy_sum").text
    dic["评论数"]=i.find("div",class_="comment_sum").text
    dic["排名"]=i.find("span",class_="ranking_sum").text
    dic["星级"]=i.find("span",class_="total_star").find("span")["style"].split(":")[1]
    dic["描述"]=i.find('div',class_="desbox").text
    datai.append(dic)


# In[68]:


df=pd.DataFrame(datai)


# In[69]:


df


# In[81]:


datai=[]
n=0

for ui in urllist:
    r=requests.get(ui)
    soup=BeautifulSoup(r.text,"lxml")
    ul=soup.find("ul",class_="list_item clrfix") 
    li=ul.find_all("li")   
    
    for i in li:
        n += 1
        dic = { }

        dic["景点名称"]=i.find("span",class_="cn_tit").text.split("：")[0]
        dic["攻略数目"]=i.find("div",class_="strategy_sum").text
        dic["评论数"]=i.find("div",class_="comment_sum").text
        dic["排名"]=i.find("span",class_="ranking_sum").text
        dic["星级"]=i.find("span",class_="total_star").find("span")["style"].split(":")[1]
        dic["描述"]=i.find('div',class_="desbox").text
        datai.append(dic)
        print("成功采集%i条数据"%n)


# In[77]:


print(datai)


# In[82]:


df=pd.DataFrame(datai)


# In[83]:


df


# In[91]:


df['星级']=df['星级'].str.replace("%"," ")
df['星级']=df['星级'].astype(np.int)
df


# In[93]:


df["排名"]=df["排名"].str.split("第").str[1]
df

