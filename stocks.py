#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install yfinance')


# In[1]:


# Imports

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf


# In[2]:


# Markdown format change

st.markdown('''
<style>
.main{
background-color: #F7F7FF;
}
<style>
''',
unsafe_allow_html= True)


# In[3]:


df = pd.read_csv('ticker_list.csv')


# In[4]:


ticker_dict = df.set_index('Name').to_dict()['Ticker']


# In[5]:


# St. text

st.write('''
# Stock Price App
''')


# In[6]:


# St. user input
st.sidebar.subheader('User Inputs')
company = st.sidebar.selectbox('Select a Company', list(ticker_dict.keys()))
start_date = st.sidebar.date_input('Start Date', pd.datetime(2015,5,31))
end_date = st.sidebar.date_input('End Date', pd.datetime(2020,5,31))


# In[7]:


# St. text

st.write('Company Name :', company)
st.write('Start Date :', start_date)
st.write('End Date :', end_date)



# In[8]:


# Get data from yfinance
ticker_symbol = ticker_dict[company]
ticker_data = yf.Ticker(ticker_symbol)
tickerdf = ticker_data.history(period='1d', start=start_date, end=end_date)


# In[9]:


tickerdf1 = tickerdf.reset_index()


# In[10]:


percent_change = round((tickerdf1.iloc[(len(tickerdf1) - 1), 4] - tickerdf1.iloc[0, 4]) / tickerdf1.iloc[(len(tickerdf1) - 1), 4] * 100, 2)


# In[11]:


# St. text and charts

st.write('Change in Stock Price =', percent_change, '%')

st.header('Closing Price')
st.line_chart(tickerdf.Close)
st.header('Volume')
st.line_chart(tickerdf.Volume)


# In[ ]:





# In[2]:


#pip freeze > 01_Google_Ticker_requirements.txt


# In[ ]:




