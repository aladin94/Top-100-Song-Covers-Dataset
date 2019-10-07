#!/usr/bin/env python
# coding: utf-8

# # Welcome to my Portfolio Project on WebScraping!

# ## In this project, I am going to analyze the Top 100 Covered Albums of All-Time. This project is definitely more personal to me as opposed to my other exercises. As an Amateur Musician, not only do I have a passion for music, but I most definitely love discovering covers of Songs/Albums where the artist provides his/her own twist to the original.

# In[561]:


#Make the necessary imports immediately to avoid errors.

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import requests 
from bs4 import BeautifulSoup 


# In[562]:


#Here we are making an HTTP request to pull the HTML code from the URL we desire.

URL = "https://secondhandsongs.com/statistics?sort=covers&list=stats_release_covers"
r = requests.get(URL) 


# In[563]:


soup = BeautifulSoup(r.content, "html5lib") 
print(soup.prettify()) 


# In[564]:


#We would like to extract the <tr> tags belonging to the table, whose id = "vw"
rows = soup.select('#vw tr')
rows


# In[565]:


frame = []
for row in rows:
    frame.append([td.text for td in row.select('td')])
    print([td.text for td in row.select('td')])


# ## Another way we could've approached this scenario would be to use Pandas, which may have been easier. However, I'd prefer to use BeautifulSoup for purposes of this example.

# In[566]:


#table = pd.read_html('https://secondhandsongs.com/statistics?sort=covers&list=stats_release_covers')[0]
#print(table)


# In[606]:


df = pd.DataFrame(frame)
df.columns = ['Rank', 'Album', 'Artist', 'Count']
df.reset_index()
df.drop(0, inplace=True)
#Remove the zero index. Now everything is ranked 1-100


# In[607]:


df.tail(20)


# In[608]:


#Create a copy of our DataFrame for some Data Visualization.
df1 = df[0:9]
df1 = df1.astype({'Count':int,'Rank':int}) #Converting the columns to be numeric, in order to be used for Plotting.


# ## We will use the Seaborn library (my favorite for Data Visualization), to create a graph to analyze the data more easily. This graph represents the top 10 covered Albums and their respective counts. We can clearly tell that for some reason, 6 of the 10 most covered records belong to The Beatles! 

# In[570]:


sns.barplot(x= "Count",y="Album",data=df1)


# In[609]:


df['Count'] = df['Count'].astype(int)


# In[610]:


df['Count'].sum()


# In[623]:


#The total Count of covers belonging to a Beatles Album:
Beatle = df.loc[df['Artist'] == 'The Beatles', 'Count'].sum()
Beatle


# In[622]:


#The total Count of covers not belonging to a Beatles Album:
Not_beatle = Beatle = df.loc[df['Artist'] != 'The Beatles', 'Count'].sum()
Not_beatle


# In[636]:


labels = ['Beatles', 'Non-Beatles']
sizes = [9977,48948]
colors = ['gold', 'yellowgreen']
explode = [0.1, 0]


# ## Using a simple Pie chart, we can see that the Beatles hold roughly 1/6 of the total number of Covers, in addition to holding the top 4 ranks. People clearly love this band!

# In[640]:


plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors = ['#66b3ff', '#99ff99'],
        shadow=True, startangle=90)
plt.tight_layout()
plt.axis('equal')  
plt.show()


# # This is the end of this project. We've conducted WebScraping & Data Manipulation/Visualization using various Python modules (BeautifulSoup, Numpy, Pandas, and Seaborn). Thanks for stopping by and please feel free to visit my Data Science blog: helloworldofdata.webnode.com
