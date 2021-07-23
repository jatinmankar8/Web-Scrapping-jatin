#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
c = r.content
soup = BeautifulSoup(c, "html.parser")
a = soup.find_all("div", {"class":"propertyRow"})
page_no = soup.find_all("a", {"class":"Page"})[-1].text


# In[3]:


list1 = []
base_url = "http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_no)*10,10):
    url = base_url + str(page)+ ".html"
    print(url)
    r = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    a = soup.find_all("div", {"class":"propertyRow"})
    
    for item in a:
        d = {}
        d["Plot Price"] = item.find("h4", {"class":"propPrice"}).text.replace("\n","").replace(" ","")
        d["Address"] = item.find_all("span", {"class":"propAddressCollapse"})[0].text
        try:
            d["Locality"] = item.find_all("span", {"class":"propAddressCollapse"})[1].text
        except:
            d["Locality"] = "None"

        try:
            d["Bed Info"] = item.find("span", {"class":"infoBed"}).find("b").text
        except:
            d["Bed Info"] = "NULL"

        try:
            d["Area Info"] = item.find("span", {"class":"infoSqFt"}).find("b").text
        except:
             d["Area Info"] = "NULL"

        try:
            d["Full Bath"] = item.find("span", {"class":"infoValueFullBath"}).find("b").text
        except:
             d["Full Bath"] = "NULL"

        try:
            d["Half Bath"] = item.find("span", {"class":"infoValueHalfBath"}).find("b").text
        except:
             d["Half Bath"] = "NULL"


        for column_group in item.find_all("div",{"class":"columnGroup"}):
            for feature_group, feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}), column_group.find_all("span", {"class":"featureName"})):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text

        list1.append(d)


# In[5]:


import pandas
data=pandas.DataFrame(list1)


# In[7]:


df.to_csv('RealEstate.csv', index= False, encoding='utf-8')

